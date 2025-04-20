# core_dag.py
from datetime import timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.ssh.operators.ssh import SSHOperator
from pendulum import datetime
from spark_config import SPARK_JOB_RESOURCES, SPARK_JOB_ARGS, SPARK_JOB_SCRIPTS_PATH
from spark_command import build_spark_submit_command


def create_etl_oltp_to_dwh_dag():
    default_args = {
        'owner': 'airflow',
        # 'email': ['hubin.smars@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=1),
    }

    with DAG(
        dag_id='etl_oltp_to_dwh_process',
        start_date=datetime(2025, 4, 20, tz="America/Toronto"),
        schedule_interval="0 2 * * *",
        description='DAG for ELT process from OLTP to DWH',
        tags=['oltp2dwh'],
        max_active_runs=1,
        default_args=default_args,
        catchup=False
    ) as dag:

        chk_oracle = EmptyOperator(task_id="chk_oracle")

        spark_oltp_to_dwh = SSHOperator(
            task_id="etl_oltp_to_dwh",
            ssh_conn_id="spark_container",    # ssh -p 22 spark
            command=
                build_spark_submit_command(
                    deploy_mode="client",
                    resources=SPARK_JOB_RESOURCES.get("etl_oltp2dwh"),
                    job_args=SPARK_JOB_ARGS.get("etl_oltp2dwh"),
                    script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_oltp2dwh")
                ),
            cmd_timeout=600,
        )

        end_of_day = EmptyOperator(task_id="pipeline_done")

        chk_oracle >> spark_oltp_to_dwh >> end_of_day

        return dag

etl_oltp_to_dwh_process = create_etl_oltp_to_dwh_dag()