# spark_config.py

"""
    control the spark resources in terms of the job level
"""
SPARK_JOB_RESOURCES = {
    "etl_oltp2dwh" : {
        "--driver-memory": "512m",
        "--executor-memory": "1g",
        "--executor-cores": "1",
        "--num-executors": "3",
        "--conf": "spark.executor.memoryOverhead=256"
    },
    "etl_dwh2olap" : {
        "--driver-memory": "512m",
        "--executor-memory": "1g",
        "--executor-cores": "1",
        "--num-executors": "3",
        "--conf": "spark.executor.memoryOverhead=256"
    },
    "etl_ods2dwd" : {
        "--driver-memory": "512m",
        "--executor-memory": "1g",
        "--executor-cores": "1",
        "--num-executors": "3",
        "--conf": "spark.executor.memoryOverhead=256",
        "--conf": "spark.port.maxRetries=50", # web UI port entries
        "--conf": "spark.yarn.am.waitTime=1200s", # avoid the task to be killed while waiting
        "--conf": "spark.yarn.stagingDir=/user/root/.sparkStaging_etl_ods2dwd_{{ ts_nodash }}"
    },
    "etl_dwd2dim" : {
        "--driver-memory": "512m",
        "--executor-memory": "1g",
        "--executor-cores": "1",
        "--num-executors": "3",
        "--conf": "spark.executor.memoryOverhead=256",
        "--conf": "spark.port.maxRetries=50", # web UI port entries
        "--conf": "spark.yarn.am.waitTime=1200s", # avoid the task to be killed while waiting
        "--conf": "spark.yarn.stagingDir=/user/root/.sparkStaging_etl_dwd2dim_{{ ts_nodash }}"
    },
    "etl_dwd2dwm" : {
        "--driver-memory": "512m",
        "--executor-memory": "1g",
        "--executor-cores": "1",
        "--num-executors": "3",
        "--conf": "spark.executor.memoryOverhead=256",
        "--conf": "spark.port.maxRetries=50", # web UI port entries
        "--conf": "spark.yarn.am.waitTime=1200s", # avoid the task to be killed while waiting
        "--conf": "spark.yarn.stagingDir=/user/root/.sparkStaging_etl_dwd2dwm_{{ ts_nodash }}"
    },
    "etl_dwm2dws" : {
        "--driver-memory": "512m",
        "--executor-memory": "1g",
        "--executor-cores": "1",
        "--num-executors": "3",
        "--conf": "spark.executor.memoryOverhead=256",
        "--conf": "spark.port.maxRetries=50", # web UI port entries
        "--conf": "spark.yarn.am.waitTime=1200s", # avoid the task to be killed while waiting
        "--conf": "spark.yarn.stagingDir=/user/root/.sparkStaging_etl_dwm2dws_{{ ts_nodash }}"
    },
}

"""
    control the spark-submit job arguments
"""
SPARK_JOB_ARGS = {
    "etl_oltp2dwh" : [
        "--job_type", "oltp_to_dwh",
        "--partition_data", "{{ ds }}"
    ],
    "etl_dwh2olap" : [
        "--job_type", "oltp_to_dwh",
        "--partition_data", "{{ ds }}"
    ],
    # ods to dwd
    "etl_ods2dwd_dwd_campaign_product_subcategory_fpd" : [
        "--job_type", "ods_to_dwd",
        "--table_name", "dwd_campaign_product_subcategory_fpd",
    ],
    "etl_ods2dwd_dwd_category_fpd" : [
        "--job_type", "ods_to_dwd",
        "--table_name", "dwd_category_fpd",
    ],
    "etl_ods2dwd_dwd_customer_fpd" : [
        "--job_type", "ods_to_dwd",
        "--table_name", "dwd_customer_fpd",
    ],
    "etl_ods2dwd_dwd_customer_product_ratings_ipd" : [
        "--job_type", "ods_to_dwd",
        "--table_name", "dwd_customer_product_ratings_ipd",
        "--partition_data", "{{ ds }}"
    ],
    "etl_ods2dwd_dwd_marketing_campaigns_fpd" : [
        "--job_type", "ods_to_dwd",
        "--table_name", "dwd_marketing_campaigns_fpd",
    ],
    "etl_ods2dwd_dwd_orderitem_ipd" : [
        "--job_type", "ods_to_dwd",
        "--table_name", "dwd_orderitem_ipd",
        "--partition_data", "{{ ds }}"
    ],
    "etl_ods2dwd_dwd_orders_ipd" : [
        "--job_type", "ods_to_dwd",
        "--table_name", "dwd_orders_ipd",
        "--partition_data", "{{ ds }}"
    ],
    "etl_ods2dwd_dwd_payment_method_fpd" : [
        "--job_type", "ods_to_dwd",
        "--table_name", "dwd_payment_method_fpd",
    ],
    "etl_ods2dwd_dwd_product_fpd" : [
        "--job_type", "ods_to_dwd",
        "--table_name", "dwd_product_fpd",
    ],
    "etl_ods2dwd_dwd_returns_ipd" : [
        "--job_type", "ods_to_dwd",
        "--table_name", "dwd_returns_ipd",
        "--partition_data", "{{ ds }}"
    ],
    "etl_ods2dwd_dwd_subcategory_fpd" : [
        "--job_type", "ods_to_dwd",
        "--table_name", "dwd_subcategory_fpd",
    ],
    "etl_ods2dwd_dwd_supplier_fpd" : [
        "--job_type", "ods_to_dwd",
        "--table_name", "dwd_supplier_fpd",
    ],

    # dwd to dim
    "etl_dwd2dim_dim_campaign_discount_fpd" : [
        "--job_type", "dwd_to_dim",
        "--table_name", "dim_campaign_discount_fpd",
    ],
    "etl_dwd2dim_dim_category_fpd" : [
        "--job_type", "dwd_to_dim",
        "--table_name", "dim_category_fpd",
    ],
    "etl_dwd2dim_dim_customer_fpd" : [
        "--job_type", "dwd_to_dim",
        "--table_name", "dim_customer_fpd",
    ],
    "etl_dwd2dim_dim_payment_method_fpd" : [
        "--job_type", "dwd_to_dim",
        "--table_name", "dim_payment_method_fpd",
    ],
    "etl_dwd2dim_dim_product_fpd" : [
        "--job_type", "dwd_to_dim",
        "--table_name", "dim_product_fpd",
    ],
    "etl_dwd2dim_dim_supplier_fpd" : [
        "--job_type", "dwd_to_dim",
        "--table_name", "dim_supplier_fpd",
    ],

    # dwd to dwm
    "etl_dwd2dwm_dwm_orders_with_items_ipd" : [
        "--job_type", "dwd_to_dwm",
        "--table_name", "dwm_orders_with_items_ipd",
        "--partition_data", "{{ ds }}"
    ],

    # dwm to dws
    "etl_dwm2dws_dws_orders_detailed_info_wide_ipd" : [
        "--job_type", "dwm_to_dws",
        "--table_name", "dws_orders_detailed_info_wide_ipd",
        "--partition_data", "{{ ds }}"
    ]
}

"""
    control the PySpark script path on the spark container 
"""
SPARK_JOB_SCRIPTS_PATH = {
    "etl_oltp2dwh" : "/opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/"
                     "big-data-engineering-project1/src/main_data_pipeline.py",
    "etl_dwh2olap" : "/opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/"
                     "big-data-engineering-project1/src/main_data_pipeline.py",
    "etl_batch_process" : "/opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/"
                          "big-data-engineering-project1/src/main_batch_processing.py",
}