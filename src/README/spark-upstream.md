# /src/data_pipeline + /src/main_data_pipeline.py

This document provides an overview of the Spark upstream data pipeline module, including its file structure, job configuration instructions, and submission guidelines for running the PySpark job in a distributed environment using YARN.

## Project Structure

The codebase is organized as follows:

```text
/src/main_batch_processing.py                      # Entry point of the PySpark program
/src/batch_processing/
    ├── config/                                 # Configuration files
    │   ├── .env                                # General environment variable settings
    │   ├── .env.secret                         # Sensitive environment variables
    │   ├── __init__.py                         # Python package marker
    │   ├── database_connection_config.py       # Database connection configuration
    │   ├── get_env.py                          # Utility to fetch environment variables
    │   ├── hadoop_env_config.py                # Hadoop environment configuration
    │   ├── hive2ck_tables_config.py            # Table mappings: Hive to ClickHouse
    │   ├── job_configs.py                      # Core pipeline job type definitions
    │   ├── logging_config.py                   # Logging configuration
    │   ├── oracle2hive_tables_config.py        # Table mappings: Oracle to Hive
    │   └── spark_env_config.py                 # Spark environment configuration
    ├── jobs/                                   # Core ETL logic modules
    │   ├── __init__.py
    │   ├── extract_oracle.py                   # Extract data from Oracle
    │   ├── load_ck.py                          # Load data from DWH into ClickHouse
    │   ├── load_hdfs.py                        # Load Hive data into HDFS
    │   ├── parse_field_type.py                 # Spark field type parsing
    │   ├── spark_downstream.py                 # Hive to OLAP (ClickHouse) pipeline
    │   └── spark_upstream.py                   # OLTP to Hive data ingestion
    ├── utils/                                  # Utility modules
    │   ├── __init__.py
    │   ├── hdfs_utils.py                      # HDFS file operations
    │   ├── logging_utils.py                   # Logging helper functions
    │   └── oracle_database_utils.py           # Oracle-specific DB utilities
    └── __init__.py
```

## Job Configuration

Before executing `main_data_pipeline.py`, ensure the following configurations are correctly set:

In lines 9–32 of the script, validate the `oltp_data_source` and `dwh_data_target` values.

These determine the source OLTP database to extract from and the target data warehouse to write into.

```text
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Job Config >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --job_type oltp_to_dwh : spark_upstream()
oltp_data_source = {
    "db_type" : "oracle",
    "instance_code" : "1"
}

dwh_data_target = {
    "dwh_type" : "hive",
    "dwh_target_db" : "ods",
}
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< End of Job Config >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
```

## Job Execution (Spark Submit)

In the `Spark` container, To execute the PySpark job in a YARN-based distributed environment (client mode), use the following command template:

```bash
spark-submit --master yarn \
--deploy-mode client \
--driver-memory 512m \
--executor-memory 1g \
--executor-cores 1 \
--num-executors 3 \
--conf "spark.executor.memoryOverhead=512" \
/opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/src/main_data_pipeline.py \
--job_type oltp_to_dwh \
--partition_data 2025-03-25
```

**Parameters**:

`--job_type`: Type of job to run. Use `oltp_to_dwh` to extract data from Oracle and load it into Hive.

`--partition_data`: Date partition for the ETL process. Format: `yyyy-MM-dd`.