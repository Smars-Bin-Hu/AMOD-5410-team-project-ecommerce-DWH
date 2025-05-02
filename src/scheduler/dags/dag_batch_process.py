# dag_etl_oltp2dwh.py
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from configs import SPARK_JOB_RESOURCES, SPARK_JOB_ARGS, SPARK_JOB_SCRIPTS_PATH, DAGConfig
from utils import build_spark_submit_command

with DAG(**DAGConfig.get("etl_daily_batch_process")) as dag:
    start_daily_batch = EmptyOperator(task_id="start_daily_batch")
    end_of_daily_batch = EmptyOperator(task_id="end_of_daily_batch")

    # <<<<<<< start of daily batch: ODS to DWD >>>>>>>>
    start_of_ods2dwd = EmptyOperator(task_id="start_of_ods2dwd")
    end_of_ods2dwd = EmptyOperator(task_id="end_of_ods2dwd")

    # ETL job - Transform from ODS to DWD - Table: dwd_campaign_product_subcategory_fpd
    spark_etl_ods2dwd_dwd_campaign_product_subcategory_fpd = SSHOperator(
        task_id="etl_ods2dwd_dwd_campaign_product_subcategory_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_ods2dwd"),
            job_args=SPARK_JOB_ARGS.get("etl_ods2dwd_dwd_campaign_product_subcategory_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from ODS to DWD - Table: dwd_category_fpd
    spark_etl_ods2dwd_dwd_category_fpd = SSHOperator(
        task_id="etl_ods2dwd_dwd_category_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_ods2dwd"),
            job_args=SPARK_JOB_ARGS.get("etl_ods2dwd_dwd_category_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from ODS to DWD - Table: dwd_customer_fpd
    spark_etl_ods2dwd_dwd_customer_fpd = SSHOperator(
        task_id="etl_ods2dwd_dwd_customer_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_ods2dwd"),
            job_args=SPARK_JOB_ARGS.get("etl_ods2dwd_dwd_customer_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from ODS to DWD - Table: dwd_customer_product_ratings_ipd
    spark_etl_ods2dwd_dwd_customer_product_ratings_ipd = SSHOperator(
        task_id="etl_ods2dwd_dwd_customer_product_ratings_ipd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_ods2dwd"),
            job_args=SPARK_JOB_ARGS.get("etl_ods2dwd_dwd_customer_product_ratings_ipd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from ODS to DWD - Table: dwd_marketing_campaigns_fpd
    spark_etl_ods2dwd_dwd_marketing_campaigns_fpd = SSHOperator(
        task_id="etl_ods2dwd_dwd_marketing_campaigns_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_ods2dwd"),
            job_args=SPARK_JOB_ARGS.get("etl_ods2dwd_dwd_marketing_campaigns_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from ODS to DWD - Table: dwd_orderitem_ipd
    spark_etl_ods2dwd_dwd_orderitem_ipd = SSHOperator(
        task_id="etl_ods2dwd_dwd_orderitem_ipd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_ods2dwd"),
            job_args=SPARK_JOB_ARGS.get("etl_ods2dwd_dwd_orderitem_ipd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from ODS to DWD - Table: dwd_orders_ipd
    spark_etl_ods2dwd_dwd_orders_ipd = SSHOperator(
        task_id="etl_ods2dwd_dwd_orders_ipd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_ods2dwd"),
            job_args=SPARK_JOB_ARGS.get("etl_ods2dwd_dwd_orders_ipd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from ODS to DWD - Table: dwd_payment_method_fpd
    spark_etl_ods2dwd_dwd_payment_method_fpd = SSHOperator(
        task_id="etl_ods2dwd_dwd_payment_method_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_ods2dwd"),
            job_args=SPARK_JOB_ARGS.get("etl_ods2dwd_dwd_payment_method_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from ODS to DWD - Table: dwd_product_fpd
    spark_etl_ods2dwd_dwd_product_fpd = SSHOperator(
        task_id="etl_ods2dwd_dwd_product_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_ods2dwd"),
            job_args=SPARK_JOB_ARGS.get("etl_ods2dwd_dwd_product_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from ODS to DWD - Table: dwd_returns_ipd
    spark_etl_ods2dwd_dwd_returns_ipd = SSHOperator(
        task_id="etl_ods2dwd_dwd_returns_ipd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_ods2dwd"),
            job_args=SPARK_JOB_ARGS.get("etl_ods2dwd_dwd_returns_ipd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from ODS to DWD - Table: dwd_subcategory_fpd
    spark_etl_ods2dwd_dwd_subcategory_fpd = SSHOperator(
        task_id="etl_ods2dwd_dwd_subcategory_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_ods2dwd"),
            job_args=SPARK_JOB_ARGS.get("etl_ods2dwd_dwd_subcategory_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from ODS to DWD - Table: dwd_supplier_fpd
    spark_etl_ods2dwd_dwd_supplier_fpd = SSHOperator(
        task_id="etl_ods2dwd_dwd_supplier_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_ods2dwd"),
            job_args=SPARK_JOB_ARGS.get("etl_ods2dwd_dwd_supplier_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )
    # <<<<<<< end of daily batch: ODS to DWD >>>>>>>>

    # trigger ods partition tables refreshing
    refresh_dwd = TriggerDagRunOperator(
        task_id="trigger_dwd_refresh",
        trigger_dag_id="backfill_refresh",
        conf={"dwh_layer": "dwd"},
        wait_for_completion=True,       # 如需等刷新完再继续
        reset_dag_run=True              # 若同一天已触发过则重新跑
    )

    # <<<<<<< start of daily batch: DWD to DIM & DWM >>>>>>>>
    start_of_dwd2dim = EmptyOperator(task_id="start_of_dwd2dim")
    start_of_dwd2dwm = EmptyOperator(task_id="start_of_dwd2dwm")
    end_of_dwd2dim = EmptyOperator(task_id="end_of_dwd2dim")
    end_of_dwd2dwm = EmptyOperator(task_id="end_of_dwd2dwm")

    # daily batch: dwd to dim
    # ETL job - Transform from DWD to DIM - Table: dim_campaign_discount_fpd
    spark_etl_dwd2dim_dim_campaign_discount_fpd = SSHOperator(
        task_id="etl_dwd2dim_dim_campaign_discount_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_dwd2dim"),
            job_args=SPARK_JOB_ARGS.get("etl_dwd2dim_dim_campaign_discount_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from DWD to DIM - Table: dim_category_fpd
    spark_etl_dwd2dim_dim_category_fpd = SSHOperator(
        task_id="etl_dwd2dim_dim_category_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_dwd2dim"),
            job_args=SPARK_JOB_ARGS.get("etl_dwd2dim_dim_category_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from DWD to DIM - Table: dim_customer_fpd
    spark_etl_dwd2dim_dim_customer_fpd = SSHOperator(
        task_id="etl_dwd2dim_dim_customer_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_dwd2dim"),
            job_args=SPARK_JOB_ARGS.get("etl_dwd2dim_dim_customer_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from DWD to DIM - Table: dim_payment_method_fpd
    spark_etl_dwd2dim_dim_payment_method_fpd = SSHOperator(
        task_id="etl_dwd2dim_dim_payment_method_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_dwd2dim"),
            job_args=SPARK_JOB_ARGS.get("etl_dwd2dim_dim_payment_method_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from DWD to DIM - Table: dim_product_fpd
    spark_etl_dwd2dim_dim_product_fpd = SSHOperator(
        task_id="etl_dwd2dim_dim_product_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_dwd2dim"),
            job_args=SPARK_JOB_ARGS.get("etl_dwd2dim_dim_product_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # ETL job - Transform from DWD to DIM - Table: dim_supplier_fpd
    spark_etl_dwd2dim_dim_supplier_fpd = SSHOperator(
        task_id="etl_dwd2dim_dim_supplier_fpd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_dwd2dim"),
            job_args=SPARK_JOB_ARGS.get("etl_dwd2dim_dim_supplier_fpd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    # daily batch: dwd to dwm
    # ETL job - Transform from DWD to DWM - Table: dim_supplier_fpd
    spark_etl_dwd2dwm_dwm_orders_with_items_ipd = SSHOperator(
        task_id="etl_dwd2dwm_dwm_orders_with_items_ipd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_dwd2dwm"),
            job_args=SPARK_JOB_ARGS.get("etl_dwd2dwm_dwm_orders_with_items_ipd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    refresh_dwm = TriggerDagRunOperator(
        task_id="trigger_dwm_refresh",
        trigger_dag_id="backfill_refresh",
        conf={"dwh_layer": "dwm"},
        wait_for_completion=True,       # 如需等刷新完再继续
        reset_dag_run=True              # 若同一天已触发过则重新跑
    )
    # <<<<<<< END of daily batch: DWD to DIM & DWM >>>>>>>>

    # <<<<<<< START of daily batch: DWM to DWS >>>>>>>>
    start_of_dwm2dws = EmptyOperator(task_id="start_of_dwm2dws")
    end_of_dwm2dws = EmptyOperator(task_id="end_of_dwm2dws")

    # ETL job - Transform from DWM to DWS - Table: dws_orders_detailed_info_wide_ipd
    spark_etl_dwm2dws_dws_orders_detailed_info_wide_ipd = SSHOperator(
        task_id="etl_dwm2dws_dws_orders_detailed_info_wide_ipd",
        ssh_conn_id="spark_container",    # ssh -p 22 spark
        command=
        build_spark_submit_command(
            deploy_mode="client",
            resources=SPARK_JOB_RESOURCES.get("etl_dwm2dws"),
            job_args=SPARK_JOB_ARGS.get("etl_dwm2dws_dws_orders_detailed_info_wide_ipd"),
            script_path=SPARK_JOB_SCRIPTS_PATH.get("etl_batch_process")
        ),
        cmd_timeout=600,
    )

    refresh_dws = TriggerDagRunOperator(
        task_id="trigger_dws_refresh",
        trigger_dag_id="backfill_refresh",
        conf={"dwh_layer": "dws"},
        wait_for_completion=True,       # 如需等刷新完再继续
        reset_dag_run=True              # 若同一天已触发过则重新跑
    )
    # <<<<<<< END of daily batch: DWM to DWS >>>>>>>>

    start_of_ods2dwd >> spark_etl_ods2dwd_dwd_campaign_product_subcategory_fpd >> end_of_ods2dwd
    start_of_ods2dwd >> spark_etl_ods2dwd_dwd_category_fpd >> end_of_ods2dwd
    start_of_ods2dwd >> spark_etl_ods2dwd_dwd_customer_fpd >> end_of_ods2dwd
    start_of_ods2dwd >> spark_etl_ods2dwd_dwd_customer_product_ratings_ipd >> end_of_ods2dwd
    start_of_ods2dwd >> spark_etl_ods2dwd_dwd_marketing_campaigns_fpd >> end_of_ods2dwd
    start_of_ods2dwd >> spark_etl_ods2dwd_dwd_orderitem_ipd >> end_of_ods2dwd
    start_of_ods2dwd >> spark_etl_ods2dwd_dwd_orders_ipd >> end_of_ods2dwd
    start_of_ods2dwd >> spark_etl_ods2dwd_dwd_payment_method_fpd >> end_of_ods2dwd
    start_of_ods2dwd >> spark_etl_ods2dwd_dwd_product_fpd >> end_of_ods2dwd
    start_of_ods2dwd >> spark_etl_ods2dwd_dwd_returns_ipd >> end_of_ods2dwd
    start_of_ods2dwd >> spark_etl_ods2dwd_dwd_subcategory_fpd >> end_of_ods2dwd
    start_of_ods2dwd >> spark_etl_ods2dwd_dwd_supplier_fpd >> end_of_ods2dwd

    end_of_ods2dwd >> refresh_dwd >> start_of_dwd2dim
    end_of_ods2dwd >> refresh_dwd >> start_of_dwd2dwm

    start_of_dwd2dim >> spark_etl_dwd2dim_dim_campaign_discount_fpd >> end_of_dwd2dim
    start_of_dwd2dim >> spark_etl_dwd2dim_dim_category_fpd >> end_of_dwd2dim
    start_of_dwd2dim >> spark_etl_dwd2dim_dim_customer_fpd >> end_of_dwd2dim
    start_of_dwd2dim >> spark_etl_dwd2dim_dim_payment_method_fpd >> end_of_dwd2dim
    start_of_dwd2dim >> spark_etl_dwd2dim_dim_product_fpd >> end_of_dwd2dim
    start_of_dwd2dim  >> spark_etl_dwd2dim_dim_supplier_fpd >> end_of_dwd2dim

    start_of_dwd2dwm >> spark_etl_dwd2dwm_dwm_orders_with_items_ipd >> end_of_dwd2dwm

    end_of_dwd2dim >> refresh_dwm >> start_of_dwm2dws
    end_of_dwd2dwm >> refresh_dwm >> start_of_dwm2dws

    start_of_dwm2dws >> spark_etl_dwm2dws_dws_orders_detailed_info_wide_ipd >> end_of_dwm2dws >> refresh_dws >> end_of_daily_batch