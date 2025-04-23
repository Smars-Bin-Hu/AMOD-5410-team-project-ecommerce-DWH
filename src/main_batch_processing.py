from pyspark.sql import SparkSession
import argparse
from .batch_processing.utils import logger
from .batch_processing.configs import job_configs
from .batch_processing.jobs import ods_to_dwd


job_functions_mapping = {
    "ods_to_dwd" : ods_to_dwd(),
    "dwd_to_dwm" : dwd_to_dwm(),
    "dwd_to_dim" : dwd_to_dim(),
    "dwm_to_dws" : dwm_to_dws(),
}

def main(args):
    current_app_name = ""
    current_launch_log = ""

    # get the job information
    if args.job_type == "ods_to_dwd":
        current_app_name = job_configs["ods_to_dwd"].get("app_name")
        current_launch_log = job_configs["ods_to_dwd"].get("launch_log")
        current_job_func = job_functions_mapping["ods_to_dwd"]
    elif args.job_type == "dwd_to_dwm":
        current_app_name = job_configs["dwd_to_dwm"].get("app_name")
        current_launch_log = job_configs["dwd_to_dwm"].get("launch_log")
        current_job_func = job_functions_mapping["dwd_to_dwm"]
    elif args.job_type == "dwd_to_dim":
        current_app_name = job_configs["dwd_to_dim"].get("app_name")
        current_launch_log = job_configs["dwd_to_dim"].get("launch_log")
        current_job_func = job_functions_mapping["dwd_to_dim"]
    elif args.job_type == "dwm_to_dws":
        current_app_name = job_configs["dwm_to_dws"].get("app_name")
        current_launch_log = job_configs["dwm_to_dws"].get("launch_log")
        current_job_func = job_functions_mapping["dwm_to_dws"]

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
    current_job_func(
        spark,
        table_name = args.table_name,
        has_partition = args.has_partition,
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
        "--has_partition",
        type=bool,
        help="Spark Batch Processing : has partition or not (bool type)"
    )
    parser.add_argument(
        "--partition_data",
        type=str,
        help="Spark Batch Procesing : Partition Field Data (str type)"
    )
    args = parser.parse_args()
    main(args)
