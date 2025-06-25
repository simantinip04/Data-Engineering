from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def greet():
    print("Hello from your first Airflow DAG!")

with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["intro"]
) as dag:
    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=greet
    )
