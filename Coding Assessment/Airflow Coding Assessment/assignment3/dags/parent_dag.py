from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

def print_hello():
    print("👋 Hello from parent DAG!")

with DAG(
    dag_id="parent_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    description="Parent DAG that triggers child DAG"
) as dag:

    start_task = PythonOperator(
        task_id="start_task",
        python_callable=print_hello
    )

    trigger_child = TriggerDagRunOperator(
        task_id="trigger_child_dag",
        trigger_dag_id="child_dag",  # Should match actual child DAG id
        conf={"triggered_by": "parent_dag", "run_date": "{{ ds }}"},  # Sending metadata
        wait_for_completion=False  # Set True if you want parent to wait
    )

    start_task >> trigger_child
