# pip install apache-airflow-providers-apache-spark
from airflow import DAG
from datetime import datetime
from airflow.providers.apache.spark.operators.spark_summit import SparkSubmitOperator

default_args = {
    'start_date' : datetime(2021,1,1)
}
with DAG(dag_id='spark-example',
         schedule_interval = '@daily',
         default_args = default_args,
         tags = ['spark'],
         catchup=False) as dag:

    subnit_job = SparkSubmitOperator(
        task_id = "sql_job",
        application = "count_trip.py",
        conn_id = "spark_local"
        )