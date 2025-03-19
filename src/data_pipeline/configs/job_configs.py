job_configs = {
    "oracle_to_hive" : {
        "app_name" : "etl_oracle_to_hdfs_pyspark_on_yarn",
        "launch_log" : "MAIN METHOD IS EXECUTED. SPARK ETL JOB IS STARTING. EXTRACT DATA FROM ORACLE TO HDFS ODS"
    },
    "hive_to_ck" : {
        "app_name" : "load_table_to_azure_cloud_clickhouse_pyspark_on_yarn",
        "launch_log" : "MAIN METHOD IS EXECUTED. SPARK ETL JOB IS STARTING. LOAD DATA FROM HIVE TO CLICKHOUSE USING SPARK ON YARN"
    }
}