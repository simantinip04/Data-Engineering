from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os

# Define file path
BASE_PATH = os.path.dirname(__file__)
ORDERS_PATH = os.path.join(BASE_PATH.replace("dags", "data"), "orders.csv")

# Define required columns
REQUIRED_COLUMNS = ["order_id", "customer_name", "product", "quantity", "price"]

def validate_data():
    print(f"🔍 Reading file from {ORDERS_PATH}")
    df = pd.read_csv(ORDERS_PATH)

    # Check columns
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise Exception(f"❌ Missing columns: {missing_columns}")

    # Check for nulls in required fields
    nulls = df[REQUIRED_COLUMNS].isnull().any()
    if nulls.any():
        raise Exception(f"❌ Null values found in: {list(nulls[nulls].index)}")

    print("✅ Validation passed.")

def summarize_data():
    df = pd.read_csv(ORDERS_PATH)
    total_quantity = df["quantity"].sum()
    total_revenue = (df["quantity"] * df["price"]).sum()

    print(f"📊 Total Quantity: {total_quantity}")
    print(f"💰 Total Revenue: ₹{total_revenue}")

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 0
}

with DAG(
    dag_id="assignment2_data_quality_validation",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description="Validate orders.csv and summarize if valid"
) as dag:

    validate = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data
    )

    summarize = PythonOperator(
        task_id="summarize_data",
        python_callable=summarize_data
    )

    validate >> summarize
