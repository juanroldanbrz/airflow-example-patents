from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators import DummyOperator, PythonOperator

import patents_crawler

default_args = {
    'owner': 'juan.roldan@bluggie.com',
    'start_date': datetime(2019, 1, 1),
    'retry_delay': timedelta(minutes=5)
}

with DAG('patent_crawler', default_args=default_args, catchup=False, schedule_interval='0 * * * *') as dag:
    """
    Airflow DAG to crawl patents.
    """

    start_task = DummyOperator(
        task_id='starting_point'
    )

    crawl_phone_patents = PythonOperator(
        task_id='crawl_phone_patents',
        python_callable=patents_crawler.crawl,
        op_kwargs={
            'keyword': 'phone'
        },
        dag=dag)

    crawl_software_patents = PythonOperator(
        task_id='crawl_software_patents',
        python_callable=patents_crawler.crawl,
        op_kwargs={
            'keyword': 'software'
        },
        dag=dag)

    # Use arrows to set dependencies between tasks
    start_task >> [crawl_phone_patents, crawl_software_patents]
