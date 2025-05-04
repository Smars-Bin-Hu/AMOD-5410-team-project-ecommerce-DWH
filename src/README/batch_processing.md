# /src/batch_processing + /src/main_batch_processing.py

## Project Structure

The codebase is organized as follows:

```text
/src/main_batch_processing.py                   # Entry point of the PySpark program
/src/batch_processing/
    ├── config/                                 # Configuration files
    │   ├── __init__.py                         # Python package marker
    │   ├── get_env.py                          # Utility to fetch environment variables
    │   ├── job_configs.py                      # Jobs configuration
    │   ├── logging_config.py                   # Logging configuration
    │   └── sql_file.py                         # SQL file information and path in terms of tables
    ├── jobs/                                   # Core ETL logic modules
    │   ├── __init__.py
    │   ├── dwd_to_dim.py                       # Core ETL Job Logic: dwd to dim
    │   ├── dwd_to_dwm.py                       # Core ETL Job Logic: dwd to dwm
    │   ├── dwm_to_dws.py                       # Core ETL Job Logic: dwm to dws
    │   └── ods_to_dwd.py                       # Core ETL Job Logic: ods to dwd
    ├── utils/                                  # Utility modules
    │   ├── __init__.py
    │   ├── read_sql.py                         # read sql file helper
    │   ├── logging_utils.py                    # Logging helper
    │   └── sql_render_partition_date.py        # render the sql by replacing the partition date helper
    ├── sql/                                    # sql DML scripts
    │   ├── dim/                                 
    │   ├── dwd/                                 
    │   ├── dwm/                                 
    │   ├── dws/                                
    │   └── all_partition_table_refresh.sql     # refresh all partition tables in the data warehouse 
    └── __init__.py
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
    /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/src/main_batch_processing.py \
--job_type ods_to_dwd 
--table_name dwd_customer_product_ratings_ipd  
--partition_data 2025-04-20
```

**Parameters**:

`--job_type`: Type of job to run. including" `ods_to_dwd`, `dwd_to_dim`, `dwd_to_dwm`, and `dwm_to_dws`.

`--table_name`: ETL job table name

`--partition_data`: Date partition for the ETL process. Format: `yyyy-MM-dd`. Could be `None`