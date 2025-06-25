import os
import shutil
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# File paths
BASE_DIR = "/opt/airflow/data"
INCOMING_FILE = os.path.join(BASE_DIR, "incoming", "report.csv")
ARCHIVE_FILE = os.path.join(BASE_DIR, "archive", "report.csv")

def process_file():
    with open(INCOMING_FILE, "r") as f:
        contents = f.read()
        print("📄 File contents:\n", contents)

def move_file():
    shutil.move(INCOMING_FILE, ARCHIVE_FILE)
    print(f"📁 Moved file to archive: {ARCHIVE_FILE}")

with DAG(
    dag_id="assignment1_file_sensor",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    description="DAG that waits for report.csv file and processes it",
) as dag:

    wait_for_file = FileSensor(
        task_id="wait_for_file",
        filepath=INCOMING_FILE,
        fs_conn_id="fs_default",  
        poke_interval=30,         
        timeout=600,              
        mode="poke",              
        soft_fail=True            
    )

    read_file = PythonOperator(
        task_id="process_file",
        python_callable=process_file
    )

    archive = PythonOperator(
        task_id="archive_file",
        python_callable=move_file
    )

    wait_for_file >> read_file >> archive
