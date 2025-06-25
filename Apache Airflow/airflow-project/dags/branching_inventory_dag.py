from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# File path
FILE_PATH = '/opt/airflow/data/inventory.csv'
THRESHOLD_SIZE = 500 * 1024  # 500 KB

# Branching function
def decide_task_based_on_size():
    file_size = os.path.getsize(FILE_PATH)
    if file_size < THRESHOLD_SIZE:
        return 'light_summary'
    else:
        return 'detailed_processing'

# Dummy processing tasks
def light_summary_task():
    print("Performing light summary...")

def detailed_processing_task():
    print("Performing detailed processing...")

def cleanup_task():
    print("Running cleanup...")

with DAG(
    dag_id='branching_inventory_processing',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    start = EmptyOperator(task_id='start')

    branching = BranchPythonOperator(
        task_id='check_file_size',
        python_callable=decide_task_based_on_size
    )

    light_summary = PythonOperator(
        task_id='light_summary',
        python_callable=light_summary_task
    )

    detailed_processing = PythonOperator(
        task_id='detailed_processing',
        python_callable=detailed_processing_task
    )

    join = EmptyOperator(task_id='join', trigger_rule='none_failed_min_one_success')

    cleanup = PythonOperator(
        task_id='cleanup',
        python_callable=cleanup_task
    )

    # DAG structure
    start >> branching
    branching >> light_summary >> join
    branching >> detailed_processing >> join
    join >> cleanup
