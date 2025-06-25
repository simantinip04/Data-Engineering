from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import time

def long_running_task():
    print("🔄 Starting long-running task...")
    time.sleep(20)  # Simulating long task
    print("✅ Completed the task successfully.")

with DAG(
    dag_id="assignment4_retry_timeout",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args={
        "retries": 3,
        "retry_delay": timedelta(seconds=10),  # delay between retries
        "retry_exponential_backoff": True,
        "execution_timeout": timedelta(seconds=30),  # hard timeout for the task
    },
    description="DAG with retry and timeout configuration"
) as dag:

    retry_timeout_task = PythonOperator(
        task_id="simulate_long_task",
        python_callable=long_running_task
    )
