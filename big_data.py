from airflow import DAG 
from datetime import datetime 
from plugins.big_data_operator import BigDataOperator


dag = DAG('big_data', description="big data dag", 
        schedule_interval=None, start_date=datetime(2024,4,1),
        catchup=False)


big_data = BigDataOperator(
    task_id='big_data',
    path_to_csv_file='/opt/airflow/data/Churn.csv',
    path_to_save_file='/opt/airflow/data/Churn.parquet',
    file_type='parquet',
    dag=dag
)

big_data 