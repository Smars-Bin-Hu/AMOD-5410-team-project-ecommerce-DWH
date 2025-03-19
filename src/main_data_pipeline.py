from pyspark.sql import SparkSession
import argparse
from data_pipeline.utils import logger
from data_pipeline.core import spark_upstream,spark_downstream
from data_pipeline.configs import job_configs

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Job Config >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --job_type oltp_to_dwh : spark_etl()
oltp_data_source = {
    "db_type" : "oracle",
    "instance_code" : "1"
}

dwh_data_target = {
    "dwh_type" : "hive",
    "dwh_target_db" : "ods",
}

# --job_type dwh_to_olap : spark_load_hive_to_ck()
dwh_data_source = {
    "dwh_type" : "hive",
    "dwh_target_db" : "dws",
}

olap_data_target = {
    "db_type" : "clickhouse",
    "instance_code" : "1"
}

partition_data = '2025-03-10'
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< End of Job Config >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def main(args):
    """
    Jar Package Dependencies:
        args.job_type == "oltp_to_dwh"
            oracle 2 hive
                /opt/spark/jars/spark-avro_2.12-3.3.0.jar
                /opt/spark/jars/ojdbc8.jar
        args.job_type == "dwh_to_olap"
            hive 2 clickhouse
                /opt/spark/jars/com.clickhouse.spark_clickhouse-spark-runtime-3.3_2.12-0.8.0.jar
                /opt/spark/jars/com.clickhouse_clickhouse-client-0.6.3.jar
                /opt/spark/jars/com.clickhouse_clickhouse-http-client-0.6.3.jar
                /opt/spark/jars/org.apache.httpcomponents.client5_httpclient5-5.2.1.jar
                /opt/spark/jars/com.clickhouse_clickhouse-data-0.6.3.jar
                /opt/spark/jars/org.apache.httpcomponents.core5_httpcore5-5.2.jar
                /opt/spark/jars/org.apache.httpcomponents.core5_httpcore5-h2-5.2.jar
                /opt/spark/jars/org.slf4j_slf4j-api-1.7.36.jar
    """
    if (
        args.job_type == "oltp_to_dwh"
     or args.job_type == "dwh_to_olap"
    # or args.job_type == "xxxx" ...
    ):
        job_config = job_configs[args.job_type]
        current_app_name = job_config.get("app_name")
        current_launch_log = job_config.get("launch_log")

        # launch spark
        logger.smars_dev(current_launch_log)
        spark = (
            SparkSession.builder
            .appName(current_app_name)
            .getOrCreate()
        )

        # call the main function
        if args.job_type == "oltp_to_dwh":
            spark_upstream(spark, oltp_data_source, dwh_data_target)
        elif args.job_type == "dwh_to_olap":
            spark_downstream(spark, dwh_data_source, olap_data_target, partition_data)

        # release resource
        spark.stop()
    else:
        logger.smars_dev("Cannot recognize the job type. please check the args --job_type  Should be:[\"oltp_to_dwh\",\"dwh_to_olap\"]")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Spark ETL Processing")
    parser.add_argument(
        "--job_type",
        type=str,
        help="Spark ETL Processing Job Type (Including: oltp_to_dwh, dwh_to_olap)"
    )
    args = parser.parse_args()
    main(args)

"""
Spark Submit Command:
spark-submit --master yarn \
    --deploy-mode client \
    --driver-memory 512m \
    --executor-memory 1g \
    --executor-cores 1 \
    --num-executors 1 \
    --conf "spark.executor.memoryOverhead=512" \
    --conf "spark.executor.memoryOverhead=256" \
    --conf spark.hadoop.yarn.log-aggregation.wait.ms=60000 \
    --conf spark.eventLog.enabled=true \
    --conf spark.eventLog.dir=hdfs:///spark-logs \
    /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/src/main_data_pipeline.py --job_type oltp_to_dwh
    
spark-submit --master yarn \
    --deploy-mode client \
    --driver-memory 512m \
    --executor-memory 1g \
    --executor-cores 1 \
    --num-executors 1 \
    --conf "spark.executor.memoryOverhead=512" \
    --conf "spark.executor.memoryOverhead=256" \
    --conf spark.hadoop.yarn.log-aggregation.wait.ms=60000 \
    --conf spark.eventLog.enabled=true \
    --conf spark.eventLog.dir=hdfs:///spark-logs \
    /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/src/main_data_pipeline.py --job_type dwh_to_olap
"""
#%%
