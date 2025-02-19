#crawling_dag.py
from datetime import datetime, timedelta
# DAG 객체 모듈
from airflow import DAG 
# 스케줄 작업 동작 함수(클래스)
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

d_arg = {
    'owner' : 'admin',
    'depends_on_pas': False,
	'start_date': datetime(2024,2,2),
    'retries':1, # 작업 실패 시 재시도 횟수
	'retry_delay':timedelta(minutes=5), # 재시도 기간(5분후 재시도)
}
# 스케줄 관리(스케줄 3개)
dag1 = DAG(
    dag_id='new_review',
    default_args=d_arg,
    start_date=datetime(2024,2,2),
    description='final project pipeline',
    schedule_interval=timedelta(days=1),    
)

# 스케줄 작업


new_review_hdfs = BashOperator(
    task_id='new_review_update',
    bash_command="hdfs dfs -rm /final/new_review.csv && hdfs dfs -put /home/lab04/note/data/new_review.csv /final",
    dag=dag1
)
new_review_dw = BashOperator(
    task_id='new_review_dw',
    cwd="/home/lab04/study/final_project",
    bash_command='python3 new_review_dw.py',
    dag=dag1
)
new_review_dm = BashOperator(
    task_id='new_review_dm',
    cwd="/home/lab04/study/final_project",
    bash_command='python3 new_review_dm.py',
    dag=dag1
)

new_review_hdfs >> new_review_dw >> new_review_dm
