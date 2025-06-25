from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from airflow.models import Variable
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime

# Define fallback email (if variable not set)
DEFAULT_EMAIL = "fallback@example.com"

def get_alert_email():
    return Variable.get("alert_email", default_var=DEFAULT_EMAIL)

def task_1_logic():
    print("✅ Task 1 executed successfully.")

def task_2_logic():
    print("✅ Task 2 executed successfully.")
    # Uncomment below to simulate failure:
    # raise Exception("❌ Simulated failure in Task 2")

def success_email_body():
    return "<h3>🎉 All tasks in the DAG completed successfully.</h3>"

def failure_email_body():
    return "<h3>⚠️ One or more tasks failed in the DAG.</h3>"

with DAG(
    dag_id="assignment6_email_notification",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args={
        "owner": "airflow",
        "email_on_failure": False,  # We'll handle it manually with EmailOperator
        "retries": 0,
    },
    description="DAG that sends email alerts on success or failure"
) as dag:

    task_1 = PythonOperator(
        task_id="task_1",
        python_callable=task_1_logic
    )

    task_2 = PythonOperator(
        task_id="task_2",
        python_callable=task_2_logic
    )

    success_email = EmailOperator(
        task_id="send_success_email",
        to=get_alert_email(),
        subject="✅ Airflow DAG Success: assignment6_email_notification",
        html_content=success_email_body(),
        trigger_rule=TriggerRule.ALL_SUCCESS
    )

    failure_email = EmailOperator(
        task_id="send_failure_email",
        to=get_alert_email(),
        subject="❌ Airflow DAG Failed: assignment6_email_notification",
        html_content=failure_email_body(),
        trigger_rule=TriggerRule.ONE_FAILED
    )

    [task_1, task_2] >> [success_email, failure_email]
