from pyspark.sql import SparkSession
import argparse
import sys
from datetime import datetime
from batch_processing.utils import logger
from batch_processing.configs import job_configs
from batch_processing.jobs import ods_to_dwd, dwd_to_dwm, dwd_to_dim, dwm_to_dws


class JobFunctionsMapping:
    def __init__(self):
        self.mapping = {
            "ods_to_dwd": ods_to_dwd,
            "dwd_to_dwm": dwd_to_dwm,
            "dwd_to_dim": dwd_to_dim,
            "dwm_to_dws": dwm_to_dws,
        }

    def get_job_function(self, job_type):
        return self.mapping.get(job_type)

    def get_valid_job_types(self):
        return list(self.mapping.keys())

job_functions_mapping = JobFunctionsMapping()

def main(args):
    # validate the partition_data
    if args.partition_data is not None:
        try:
            # check the format whether is yyyy-MM-dd or not
            args.partition_date = datetime.strptime(args.partition_data, "%Y-%m-%d")
            logger.smars_dev(f"[INFO] Valid partition_data received: {args.partition_data}")
        except ValueError:
            logger.smars_dev(f"[ERROR] Invalid date format for --partition_data: '{args.partition_data}'. "
                             f"Expected format is yyyy-MM-dd, e.g., 2025-04-19.")
            sys.exit(1)

    # validate the passing job type
    if args.job_type not in job_functions_mapping.mapping:
        logger.smars_dev(f"[ERROR] Invalid job type: '{args.job_type}'. "
                         f"Valid job types are: {list(job_functions_mapping.keys())}.")
        sys.exit(1)

    current_app_name = ""
    current_launch_log = ""

    # get the job information
    if args.job_type == "ods_to_dwd":
        current_app_name = job_configs["ods_to_dwd"].get("app_name")
        current_launch_log = job_configs["ods_to_dwd"].get("launch_log")
    elif args.job_type == "dwd_to_dwm":
        current_app_name = job_configs["dwd_to_dwm"].get("app_name")
        current_launch_log = job_configs["dwd_to_dwm"].get("launch_log")
    elif args.job_type == "dwd_to_dim":
        current_app_name = job_configs["dwd_to_dim"].get("app_name")
        current_launch_log = job_configs["dwd_to_dim"].get("launch_log")
    elif args.job_type == "dwm_to_dws":
        current_app_name = job_configs["dwm_to_dws"].get("app_name")
        current_launch_log = job_configs["dwm_to_dws"].get("launch_log")

    # print the log for current job
    logger.smars_dev(current_launch_log)

    # get the spark instance
    spark = (
        SparkSession.builder
        .appName(current_app_name)
        .enableHiveSupport()  # 一般也需要启用 Hive 支持
        .config("spark.sql.parquet.writeLegacyFormat", "true")
        # timestamp or date field compatible: .config("spark.sql.parquet.int96AsTimestamp", "true")
        .getOrCreate()
    )

    # Core function for current job
    current_job_func = job_functions_mapping.get_job_function(args.job_type)
    current_job_func(
        spark,
        table_name = args.table_name,
        partition_data = args.partition_data,
    )

    # release resource
    spark.stop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Spark Data Batch Processing")
    parser.add_argument(
        "--job_type",
        type=str,
        help="Spark Batch Processing Job Type (Including: ods_to_dwd, dwd_to_dwm, dwm_to_dws, dws_to_dwt, dwd_to_dim, dwt_to_ads)"
    )
    parser.add_argument(
        "--table_name",
        type=str,
        help="Spark Batch Processing : Table Name (str type)"
    )
    parser.add_argument(
        "--partition_data",
        type=str,
        default=None,
        help="partition data for tables entering into DWH, use the current date (format: yyyy-MM-dd) by default"
    )
    args = parser.parse_args()
    main(args)

"""
spark-submit --master yarn \
    --deploy-mode client \
    --driver-memory 512m \
    --executor-memory 1g \
    --executor-cores 1 \
    --num-executors 3 \
    --conf "spark.executor.memoryOverhead=512" \
    /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/src/main_batch_processing.py --job_type ods_to_dwd --table_name dml_dwd_customer_product_ratings_ipd  --partition_data 2025-04-20
    
"""