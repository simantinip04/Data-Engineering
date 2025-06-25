from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import os
import pandas as pd

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False
}

CSV_PATH = '/opt/airflow/data/customers.csv'

def check_file_exists():
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"{CSV_PATH} not found.")

def count_csv_rows():
    df = pd.read_csv(CSV_PATH)
    row_count = len(df)
    print(f"Total rows: {row_count}")
    return row_count

def log_row_count(ti):
    row_count = ti.xcom_pull(task_ids='count_rows')
    print(f"✅ Row count is {row_count}")

with DAG(
    dag_id='csv_to_summary_dag',
    default_args=default_args,
    schedule_interval=None,
    description='Reads CSV, counts rows, logs, and conditionally sends message',
    tags=['assignment', 'csv'],
) as dag:

    t1 = PythonOperator(
        task_id='check_file',
        python_callable=check_file_exists,
    )

    t2 = PythonOperator(
        task_id='count_rows',
        python_callable=count_csv_rows,
    )

    t3 = PythonOperator(
        task_id='log_count',
        python_callable=log_row_count,
    )

    t4 = BashOperator(
        task_id='notify_high_count',
        bash_command='echo "⚠️ More than 100 customers found in CSV!"',
        trigger_rule='all_done',
    )

    # Define flow
    t1 >> t2 >> t3 >> t4

    from airflow.models.baseoperator import chain
    from airflow.operators.python import BranchPythonOperator
    from airflow.operators.empty import EmptyOperator

    def check_if_high(ti):
        count = ti.xcom_pull(task_ids='count_rows')
        if count > 100:
            return 'notify_high_count'
        else:
            return 'no_notification'

    branch = BranchPythonOperator(
        task_id='branch_on_count',
        python_callable=check_if_high,
    )

    no_notify = EmptyOperator(
        task_id='no_notification'
    )

    t3 >> branch
    branch >> t4
    branch >> no_notify
