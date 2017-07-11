from datetime import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

def print_hello():
    return 'Hello world!'

def task2():
    return 'task2'

def task3():
    return 'task3'

default_args = {
    'owner': 'me',
    'depends_on_past': False,
    'start_date': datetime(2016, 10, 4),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

# dag = DAG(
#     'my_dag', default_args=default_args, schedule_interval=timedelta(seconds=1))

dag = DAG(
    'my_new_dag',
    description = 'My simple dag',
    schedule_interval=timedelta(minutes=1),
    start_date = datetime(2017,7,6)
    )

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = PythonOperator(
    task_id = 'hello_task',
    python_callable = print_hello,
    dag = dag)

t2 = PythonOperator(
    task_id = 'task_2',
    python_callable = task2,
    dag=dag)

t3 = PythonOperator(
    task_id = 'task_3',
    python_callable = task3,
    dag=dag)

t2.set_upstream(t1)
t3.set_upstream(t1)

# t1.set_upstream(t4)
# t2.set_upstream(t1)
# t3.set_upstream(t1)
