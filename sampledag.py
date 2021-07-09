from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

seven_days_ago = datetime.combine(datetime.today() - timedelta(7),
                                datetime.min.time())

default_args = {
  'owner': 'Airflow',
  'depends_on_past': False,
  'start_date': seven_days_ago,
  'email': ['airflow@airflow.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 1,
  'retry_delay': timedelta(minutes=30),
}
dag = DAG(ls_example', description='ls_example',
        schedule_interval='* * * * *', default_args=default_args)

t0 = BashOperator(task_id='jup_run',
                bash_command="ls -la"
                dag=dag)

t0
