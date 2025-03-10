from pyspark.sql import SparkSession
from data_pipeline.utils import logger
from data_pipeline.core import spark_etl

if __name__ == '__main__':
    logger.smars_dev("MAIN METHOD IS EXECUTED. SPARK ETL JOB IS STARTING")

    # launch spark
    spark = (
        SparkSession.builder
        .appName("etl_oracle_to_hdfs_pyspark_on_yarn")
        .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.3.0")
        .getOrCreate()
    )

    # call the data_pipeline.core.spark_etl
    spark_etl(spark)

    # release resource
    spark.stop()
