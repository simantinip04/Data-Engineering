from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.utils.trigger_rule import TriggerRule
import random
import logging
import time

default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': 10,  # seconds (will be used for exponential backoff in logic)
}

dag = DAG(
    dag_id='retry_with_alert_dag',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
    tags=['assignment', 'retry'],
)


def flaky_api():
    """Simulate an API that fails randomly."""
    wait = 2 ** random.randint(0, 3)
    time.sleep(wait)
    if random.random() < 0.5:  # 50% chance to fail
        logging.error("❌ Flaky API call failed!")
        raise Exception("Random API failure")
    logging.info("✅ Flaky API call succeeded!")


def on_failure_alert(context):
    """Send an alert/log a message after final failure."""
    task_instance = context.get('task_instance')
    logging.error(f"🚨 ALERT: Task {task_instance.task_id} failed after all retries!")


def dependent_task():
    """Runs only if flaky_api succeeds."""
    logging.info("🎯 Dependent task ran successfully because API task succeeded.")


flaky_task = PythonOperator(
    task_id='flaky_api_call',
    python_callable=flaky_api,
    on_failure_callback=on_failure_alert,
    retries=3,
    retry_exponential_backoff=True,
    retry_delay=10,
    dag=dag,
)

bonus_task = PythonOperator(
    task_id='run_if_success',
    python_callable=dependent_task,
    trigger_rule=TriggerRule.ALL_SUCCESS,
    dag=dag,
)

flaky_task >> bonus_task
