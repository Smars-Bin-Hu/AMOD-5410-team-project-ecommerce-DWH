from datetime import timedelta
from pendulum import datetime

class DAGConfig:
    @staticmethod
    def base_args(retry_minutes=1):
        return {
            "owner": "airflow",
            "email_on_failure": False,
            "email_on_retry": False,
            "retries": 2,
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
            "ods_to_dwd_process": {
                "dag_id": name,
                "start_date": datetime(2025, 4, 21, tz="America/Toronto"),
                "schedule_interval": "30 2 * * *",
                "description": "ODS → DWD, level = single table",
                "tags": ["ods2dwd"],
                "max_active_runs": 1,
                "catchup": False,
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
