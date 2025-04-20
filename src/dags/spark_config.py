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
}

"""
    control the PySpark script path on the spark container 
"""
SPARK_JOB_SCRIPTS_PATH = {
    "etl_oltp2dwh" : "/opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/"
                     "big-data-engineering-project1/src/main_data_pipeline.py",
    "etl_dwh2olap" : "/opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/"
                     "big-data-engineering-project1/src/main_data_pipeline.py",
}