from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'me',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='hello_airflow',
    default_args=default_args,
    description='A simple Hello World DAG',
    schedule=None,     # manual trigger only, changed from schedule_interval
    catchup=False,
) as dag:
    t1 = BashOperator(
        task_id='print_date',
        bash_command='echo "Today is $(date)"'
    )

    t2 = BashOperator(
        task_id='sleep',
        bash_command='sleep 5'
    )

    t1 >> t2
