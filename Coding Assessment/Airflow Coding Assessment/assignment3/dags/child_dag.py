from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_child_info(**context):
    conf = context["dag_run"].conf or {}
    print("🚀 Child DAG triggered!")
    print(f"📅 Metadata received: {conf}")

with DAG(
    dag_id="child_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,  # Only runs when triggered
    catchup=False,
    description="Child DAG triggered by parent DAG"
) as dag:

    child_task = PythonOperator(
        task_id="child_task",
        python_callable=print_child_info,
        provide_context=True
    )
