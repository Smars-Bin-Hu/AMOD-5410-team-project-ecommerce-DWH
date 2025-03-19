from pyspark.sql import SparkSession
import argparse
from data_pipeline.utils import logger
from data_pipeline.core import spark_etl,spark_load_hive_to_ck
from data_pipeline.configs import job_configs

job_functions_mapping = {
    "oracle_to_hive" : spark_etl,
    "hive_to_ck" : spark_load_hive_to_ck
}

def main(args):
    """
    Jar Package Dependencies:
        args.job_type == "oracle_to_hive"
            /opt/spark/jars/spark-avro_2.12-3.3.0.jar
        args.job_type == "oracle_to_hive"
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
        args.job_type == "oracle_to_hive"
     or args.job_type == "hive_to_ck"
    # or args.job_type == "xxxx" ...
    ):
        job_config = job_configs[args.job_type]
        current_app_name = job_config.get("app_name")
        current_launch_log = job_config.get("launch_log")
        current_job_func = job_functions_mapping[args.job_type]

        # launch spark
        logger.smars_dev(current_launch_log)
        spark = (
            SparkSession.builder
            .appName(current_app_name)
            .getOrCreate()
        )

        # call the data_pipeline.core.spark_etl
        current_job_func(spark)

        # release resource
        spark.stop()
    else:
        logger.smars_dev("Cannot recognize the job type. please check the args --job_type  Should be:[\"oracle_to_hive\",\"hive_to_ck\"]")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Spark ETL Processing")
    parser.add_argument(
        "--job_type",
        type=str,
        help="Spark ETL Processing Job Type (Including: oracle_to_hive, hive_to_ck)"
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
    /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/src/main_data_pipeline.py --job_type oracle_to_hive
    
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
    /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/src/main_data_pipeline.py --job_type hive_to_ck
"""
#%%
