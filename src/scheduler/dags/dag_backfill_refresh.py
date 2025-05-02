# dag_backfill_refresh.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.providers.ssh.operators.ssh import SSHOperator
from configs import DAGConfig, hql_files_path
from utils import read_sql, build_beeline_command

def choose_hql(**ctx):
    # "ods" / "dwd" / "dwm" / "dws"
    dwh_layer = ctx["dag_run"].conf.get("dwh_layer")

    # validate the parameter dwh_layer
    valid = ["ods", "dwd", "dws", "dwm"]
    if dwh_layer not in valid:
        raise ValueError(f"Invalid dwh_layer: {dwh_layer}. Valid options are: \"ods\" / \"dwd\" / \"dwm\" / \"dws\"")

    # get the path of the hql file
    path = hql_files_path[f"{dwh_layer}_partition_tbls_refresh"]
    sql = read_sql(path)
    return sql   # <- XCom

with DAG(**DAGConfig.get("backfill_refresh")) as dag:
    start_of_dag = EmptyOperator(task_id="start")

    # 2nd dag: choose the hql
    choose_hql = PythonOperator(
        task_id="choose_hql",
        python_callable=choose_hql,
        provide_context=True,
    )

    # 3rd dag: partition tables refresh
    run_hive_sql = SSHOperator(
        task_id="partition_tables_refresh",
        ssh_conn_id="hive_container",    # ssh -p 22 hive
        command=build_beeline_command("{{ti.xcom_pull(task_ids='choose_hql')}}"),
        cmd_timeout=600,
    )

    end_of_dag = EmptyOperator(task_id="done")

    start_of_dag >> choose_hql >> run_hive_sql >> end_of_dag