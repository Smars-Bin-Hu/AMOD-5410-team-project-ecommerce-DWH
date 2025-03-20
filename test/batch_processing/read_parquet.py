from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Check Parquet") \
    .enableHiveSupport() \
    .getOrCreate()

df = spark.read.parquet("hdfs://ns-ha/user/hive/warehouse/dwd/dwd_campaign_product_subcategory_fpd")
df.show(10)
df.printSchema()

