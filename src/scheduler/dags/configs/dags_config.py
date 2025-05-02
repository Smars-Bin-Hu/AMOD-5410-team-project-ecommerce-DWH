from datetime import timedelta
from pendulum import datetime

class DAGConfig:
    @staticmethod
    def base_args(retry_minutes=1):
        return {
            "owner": "airflow",
            "email_on_failure": False,
            "email_on_retry": False,
            "retries": 4,
            "retry_delay": timedelta(minutes=retry_minutes),
        }

    @staticmethod
    def get(name: str) -> dict:
        configs = {
            "etl_oltp_to_dwh_process": {
                "dag_id": name,
                "start_date": datetime(2025, 4, 20, tz="America/Toronto"),
                "schedule_interval": "0 2 * * *",
                "description": "OLTP → DWH, level = all tables batch",
                "tags": ["oltp2dwh"],
                "max_active_runs": 1,
                "catchup": False,
                "default_args": DAGConfig.base_args(),
            },
            "etl_daily_batch_process": {
                "dag_id": name,
                "start_date": datetime(2025, 4, 21, tz="America/Toronto"),
                "schedule_interval": "15 2 * * *",
                "description": "Daily batch processing: ODS → DWD -> DWM/DIM -> DWS -> DWT, level = single table",
                "tags": ["daily_batch"],
                "max_active_runs": 1,
                "catchup": False,
                "concurrency" : 5,
                "default_args": DAGConfig.base_args(retry_minutes=2),
            },
            "backfill_refresh" : {
                "dag_id": name,
                "start_date": datetime(2025, 4, 20, tz="America/Toronto"),
                "schedule_interval": None,
                "description": "refresh partition tables",
                "tags": ["refresh_partition_tbls"],
                "max_active_runs": 1,
                "catchup": False,
                "default_args": DAGConfig.base_args(),
            }
        }
        return configs[name]
