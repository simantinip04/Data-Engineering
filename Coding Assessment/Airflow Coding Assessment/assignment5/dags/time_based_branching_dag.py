from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime
import pendulum

def check_day_and_time():
    now = pendulum.now("Asia/Kolkata")  
    weekday = now.weekday()  
    hour = now.hour

    print(f"📆 Today is {now.format('dddd')} at {now.format('HH:mm')}")

    if weekday >= 5:
        print("🛑 It's a weekend. Skipping DAG.")
        return "skip_dag"
    elif hour < 12:
        print("🌅 Morning time. Running Task A.")
        return "task_a"
    else:
        print("🌇 Afternoon time. Running Task B.")
        return "task_b"

def task_a_logic():
    print("✅ Task A executed: Good Morning!")

def task_b_logic():
    print("✅ Task B executed: Good Afternoon!")

def cleanup():
    print("🧹 Final cleanup done.")

with DAG(
    dag_id="assignment5_time_based_branching",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    description="DAG with time-based branching and weekend skip"
) as dag:

    check_time = BranchPythonOperator(
        task_id="check_time",
        python_callable=check_day_and_time
    )

    task_a = PythonOperator(
        task_id="task_a",
        python_callable=task_a_logic
    )

    task_b = PythonOperator(
        task_id="task_b",
        python_callable=task_b_logic
    )

    skip_dag = DummyOperator(
        task_id="skip_dag"
    )

    final_cleanup = PythonOperator(
        task_id="final_cleanup",
        python_callable=cleanup,
        trigger_rule="none_failed_min_one_success"  
    )

    check_time >> [task_a, task_b, skip_dag]
    [task_a, task_b, skip_dag] >> final_cleanup
