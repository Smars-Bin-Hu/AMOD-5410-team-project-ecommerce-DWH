# 必选:导入airflow的DAG工作流
from datetime import timedelta
from airflow import DAG
# 必选:导入具体的TaskOperator类型
from airflow.operators.empty import EmptyOperator
from airflow.providers.ssh.operators.ssh import SSHOperator
# 可选:导入定时工具的包
from pendulum import datetime


# 当前工作流的基础配置
default_args = {
    'owner': 'airflow',
    'email': ['hubin.smars@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
}

# 定义当前工作流的DAG对象
with DAG(
    'dwh_elt_process',
    start_date=datetime(2025, 4, 18, tz="America/Toronto"),
    schedule_interval="0 2 * * *",
    description='first airflow task DAG',
    tags=['oltp2dwh'],
    max_active_runs=1,
    default_args=default_args,
) as dag:
    chk_oracle = EmptyOperator(task_id="chk_oracle")   # 可替换成 SQLSensor

    SPARK_RESOURCES = {
        "--driver-memory": "512m",
        "--executor-memory": "1g",
        "--executor-cores": "1",
        "--num-executors": "3",
        "--conf": "spark.executor.memoryOverhead=256"
    }

    SPARK_JOB_ARGS = [
        "--job_type", "oltp_to_dwh",
        "--partition_data", "{{ ds }}"
    ]

    spark_ssh_cmd = f"""
    spark-submit --master yarn --deploy-mode client \
        {" ".join([f"{k} {v}" for k, v in SPARK_RESOURCES.items()])} \
        /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/src/main_data_pipeline.py \
        {" ".join(SPARK_JOB_ARGS)}
    """

    spark_oltp_to_dwh = SSHOperator(
        task_id="spark_oltp_to_dwh",
        ssh_conn_id="spark_ssh",        # 你在 Airflow Connections 中配置的 SSH 连接 ID
        command=spark_ssh_cmd,
        cmd_timeout=600,
    )

    end_of_day = EmptyOperator(task_id="pipeline_done")

    chk_oracle >> hdfs_partition_create >> spark_oltp_to_dwh >> end_of_day