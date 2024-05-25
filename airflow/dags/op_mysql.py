from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator


with DAG(
    dag_id='op_mysql',
    start_date=datetime(2024, 5, 11),
    catchup=False,
    schedule_interval="@daily"
) as dag:
    start = EmptyOperator(task_id='start')

    create_new_table = MySqlOperator(
        task_id='create_new_table',
        mysql_conn_id='MYSQL_CONN',
        sql="CREATE TABLE IF NOT EXISTS students (student_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256));",
    )

    insert_data = MySqlOperator(
        task_id='insert_data',
        mysql_conn_id='MYSQL_CONN',
        sql="INSERT INTO students (name) VALUES ('Alex Jones');",
    )

    end = EmptyOperator(task_id='end')

start >> create_new_table >> insert_data >> end
