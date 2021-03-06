"""
copied from AirFlow's test_dag_v1.
This dag only runs some simple tasks to test Airflow's task execution.
"""
from datetime import datetime, timedelta

from airflow import DAG
from airflow import utils
from airflow.operators.dummy_operator import DummyOperator

now = datetime.now()
now_to_the_hour = (
    now - timedelta(0, 0, 0, 0, 0, 3)
).replace(minute=0, second=0, microsecond=0)
START_DATE = now_to_the_hour
DAG_NAME = 'oliver-dag-one'

default_args = {
    'owner': 'airflow',
    'depends_on_past': True,
    'start_date': utils.dates.days_ago(2)
}
dag = DAG(DAG_NAME, schedule_interval='*/10 * * * *', default_args=default_args)

run_this_1 = DummyOperator(task_id='run_this_1', dag=dag)
run_this_2 = DummyOperator(task_id='run_this_2', dag=dag)
run_this_2.set_upstream(run_this_1)
run_this_3 = DummyOperator(task_id='run_this_3', dag=dag)
run_this_3.set_upstream(run_this_2)
