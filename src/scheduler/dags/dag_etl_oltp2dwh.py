# dag_etl_oltp2dwh.py
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from configs import SPARK_JOB_RESOURCES, SPARK_JOB_ARGS, SPARK_JOB_SCRIPTS_PATH, DAGConfig
from utils import build_spark_submit_command

with DAG(**DAGConfig.get("etl_oltp_to_dwh_process")) as dag:
    chk_oracle = EmptyOperator(task_id="start")

    # 2nd dag: ETL job - Extract&Load data from OLTP database to DWH
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

    # 3rd dag: trigger ods partition tables refreshing
    refresh_ods = TriggerDagRunOperator(
        task_id="trigger_ods_refresh",
        trigger_dag_id="backfill_refresh",
        conf={"dwh_layer": "ods"},
        wait_for_completion=True,       # 如需等刷新完再继续
        reset_dag_run=True              # 若同一天已触发过则重新跑
    )

    end_of_task = EmptyOperator(task_id="done")

    chk_oracle >> spark_oltp_to_dwh >> refresh_ods >> end_of_task