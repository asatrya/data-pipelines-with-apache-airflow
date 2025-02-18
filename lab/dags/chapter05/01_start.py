import airflow

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator


with DAG(
    dag_id="05_01_start",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
) as dag:
    start = DummyOperator(task_id="start")

    fetch_sales = DummyOperator(task_id="fetch_sales")
    clean_sales = DummyOperator(task_id="clean_sales")

    fetch_weather = DummyOperator(task_id="fetch_weather")
    clean_weather = DummyOperator(task_id="clean_weather")

    join_datasets = DummyOperator(task_id="join_datasets")
    train_model = DummyOperator(task_id="train_model")
    deploy_model = DummyOperator(task_id="deploy_model")

    start >> [fetch_sales, fetch_weather]           # @NOTE fan-out (one-to-multiple) dependency
    fetch_sales >> clean_sales                      # @NOTE linear dependencies
    fetch_weather >> clean_weather
    [clean_sales, clean_weather] >> join_datasets   # @NOTE fan-in (multiple-to-one) dependency
    join_datasets >> train_model >> deploy_model
