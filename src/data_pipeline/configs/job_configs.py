job_configs = {
    "oltp_to_dwh" : {
        "app_name" : "etl_oracle_to_hdfs_pyspark_on_yarn",
        "launch_log" : "MAIN METHOD IS EXECUTED. SPARK ETL JOB IS STARTING. EXTRACT DATA FROM OLTP DB TO DATA WAREHOUSE USING SPARK ON YARN"
    },
    "dwh_to_olap" : {
        "app_name" : "load_data_from_dwh_to_olap",
        "launch_log" : "MAIN METHOD IS EXECUTED. SPARK ETL JOB IS STARTING. LOAD DATA FROM DATA WAREHOUSE  TO OLAP USING SPARK ON YARN"
    }
}