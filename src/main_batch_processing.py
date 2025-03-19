from pyspark.sql import SparkSession
import argparse
from .batch_processing.utils import logger
from .batch_processing.configs import job_configs
from .batch_processing.jobs import ods_to_dwd


job_functions_mapping = {
    "ods_to_dwd" : ods_to_dwd()
}

def main(args):
    current_app_name = ""
    current_launch_log = ""

    # launch spark
    if args.job_type == "ods_to_dwd":
        current_app_name = job_configs["dwd_to_dwm"].get("app_name")
        current_launch_log = job_configs["dwd_to_dwm"].get("launch_log")
        current_job_func = job_functions_mapping["dwd_to_dwm"]
    elif args.job_type == "dwd_to_dwm":
        current_app_name = job_configs["dwd_to_dwm"].get("app_name")
        current_launch_log = job_configs["dwd_to_dwm"].get("launch_log")
        current_job_func = job_functions_mapping["dwd_to_dwm"]

    logger.smars_dev(current_launch_log)

    spark = (
        SparkSession.builder
        .appName(current_app_name)
        .enableHiveSupport()  # 一般也需要启用 Hive 支持
        .config("spark.sql.parquet.writeLegacyFormat", "true")
        # timestamp or date field compatible: .config("spark.sql.parquet.int96AsTimestamp", "true")
        .getOrCreate()
    )

    # Core
    current_job_func(spark)

    # release resource
    spark.stop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Spark Data Batch Processing")
    parser.add_argument(
        "--job_type",
        type=str,
        help="Spark Batch Processing Job Type (Including: ods_to_dwd, dwd_to_dwm, dwm_to_dws, dws_to_dwt, dwd_to_dim, dwt_to_ads)"
    )
    args = parser.parse_args()
    main(args)
