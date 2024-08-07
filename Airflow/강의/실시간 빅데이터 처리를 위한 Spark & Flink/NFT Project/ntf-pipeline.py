from datetime import datetime
from airflow import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import json
from pandas import json_normalize

default_args = {
    'start_date' : datetime(2021,1,1),

}
def _processing_nft():
    assets = ti.xcom_pull(task_ids = ["extract_nft"])
    if not len(assets):
        raise ValueError("assets is empty")
    
    nft = assets[0]['assets'][0]
    processed_nft = json_normalize({
        'token_id' : nft['token_id'],
        'name' : nft['name'],
        'image_url' : nft['image_url']
    })
    processed_nft.to_csv('/tmp/processed_nft.csv', index= None,header=None)

with DAG(dag_id = 'nft-pipeline',
         schedule_interval = '@daily',
         default_args = default_args,
         tags = ['nft'],
         catchup = False) as dag:
    
    # 테이블 생성
    creating_table = SqliteOperator(
        task_id = 'creating_table',
        sqlite_conn_id = 'db_sqlite',
        sql ='''
        CREATE TABLE IF NOT EXISTS nfts(
            token_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            image_url TEXT NOT NULL
        )
        '''
    )

    # HTTP 요청 가능여부 확인
    is_api_available = HttpSensor(
        task_id = 'is_api_available',
        http_conn_id = 'opensea_api',
        endpoint = ''
    )

    # 데이터 추출
    extract_nft = SimpleHttpOperator(
        task_id = 'extract_nft',
        http_conn_id = 'opensea_api',
        endpoint = '',
        method = 'GET',
        response_filter = lambda res : json.loads(res.text),
        log_response = True
    )

    # 데이터 가공
    process_nft = PythonOperator(
        task_id = 'process_nft',
        python_callable = _processing_nft
    )

    # 데이터 저장
    store_nft = BashOperator(
        task_id = 'store_nft',
        bash_command = 'echo -e ".seperator ","\n.import /tmp/processed_nft.csv nfts | sqlite3 airflow/airflow.db'
    )


    # 의존성
    creating_table >> is_api_available >> extract_nft >> process_nft >> store_nft