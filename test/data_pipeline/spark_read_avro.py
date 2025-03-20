import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format, current_date
from pyspark.sql.types import IntegerType, StringType, DecimalType

spark = SparkSession.builder \
    .appName("OracleExtractionByPySpark") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.3.0") \
    .getOrCreate()

spark.read.format("avro").load("hdfs://ns-ha/user/hive/warehouse/ods/ods_customer_product_ratings_ipd/data_date=2025-03-08").show()
