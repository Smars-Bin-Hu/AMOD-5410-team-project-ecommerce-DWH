# /src/scheduler

## Airflow Scheduler Directory Structure

This module defines the Airflow DAGs and supporting configuration/utilities for orchestrating distributed ETL and batch jobs.

```text
scheduler/
├── dags/                                      # Root directory for all Airflow DAG logic
│   ├── configs/                               # DAG-level configuration files
│   │   ├── __init__.py
│   │   ├── dags_config.py                     # DAG parameter definitions (e.g., schedule_interval, default_args)
│   │   ├── hql_files_path_config.py           # File paths for associated .hql scripts
│   │   ├── spark_config.py                    # Spark job parameters (e.g., memory, cores, execution mode)
│   │   └── hql/                               # SQL scripts for partitioned table refresh logic
│   │       ├── dwd_partition_tbls_refresh.hql
│   │       ├── dwm_partition_tbls_refresh.hql
│   │       ├── dws_partition_tbls_refresh.hql
│   │       └── ods_partition_tbls_refresh.hql
│
│   ├── utils/                                 # Common utility functions and helpers for DAGs
│   │   ├── __init__.py
│   │   ├── build_beeline_command.py           # Construct CLI commands for Beeline execution
│   │   ├── build_spark_submit_command.py      # Construct Spark submit CLI commands
│   │   └── read_sql.py                        # Utility for reading HQL file content
│
│   ├── dag_backfill_refresh.py                # DAG for partitioned table refreshing
│   ├── dag_batch_process.py                   # DAG for scheduled daily batch transformations
│   └── dag_etl_oltp2dwh.py                    # DAG for ETL from OLTP (Oracle) to data warehouse (Hive)
```

Notes:

- Each `.hql` file in `configs/hql/` contains the logic for refreshing partitioned tables in specific layers of the data warehouse (ODS, DWD, DWM, DWS).

- `build_*_command.py` scripts dynamically generate execution commands for Spark and Hive jobs.

- Each DAG script corresponds to a distinct workflow in the data pipeline lifecycle (ETL ingestion, batch transformation, backfill operations).

## Docker `airflow` container volume mounts

```text
- ./src/scheduler/dags:/opt/airflow/dags
```