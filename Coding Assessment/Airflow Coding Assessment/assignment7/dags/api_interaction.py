from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import json
import os

# SpaceX API for latest launch
API_URL = "https://api.spacexdata.com/v4/launches/latest"
OUTPUT_FILE = "/opt/airflow/data/spacex_latest_launch.json"

def fetch_spacex_data():
    print(f"🔍 Requesting data from: {API_URL}")
    response = requests.get(API_URL)

    # Step 4: Fail the DAG if response is not 200
    if response.status_code != 200:
        raise Exception(f"❌ API call failed with status code: {response.status_code}")

    # Step 2: Parse response
    data = response.json()
    launch_name = data.get("name")
    launch_date = data.get("date_utc")
    rocket_id = data.get("rocket")
    success = data.get("success")

    parsed = {
        "launch_name": launch_name,
        "launch_date_utc": launch_date,
        "rocket_id": rocket_id,
        "success": success
    }

    print(f"🚀 Latest Launch: {launch_name} | Date: {launch_date} | Success: {success}")

    # Step 3: Save to file
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(parsed, f, indent=4)
        print(f"📁 Data saved to: {OUTPUT_FILE}")

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="assignment7_api_interaction",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description="DAG that fetches latest SpaceX launch details from a public API"
) as dag:

    fetch_api_data = PythonOperator(
        task_id="fetch_spacex_data",
        python_callable=fetch_spacex_data
    )
