from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("generate hive compatible Parquet") \
    .enableHiveSupport() \
    .getOrCreate()

spark.conf.set("spark.sql.parquet.writeLegacyFormat", "true")

df = spark.read.parquet("hdfs://ns-ha/user/hive/warehouse/dwd/dwd_campaign_product_subcategory_fpd")
# df.show(10)
# df.printSchema()
df.write \
    .mode("overwrite") \
    .option("compression", "snappy") \
    .parquet("hdfs://ns-ha/user/hive/warehouse/dwd/dwd_campaign_product_subcategory_fpd_compat")

"""on the hive
INSERT OVERWRITE TABLE dwd.dwd_campaign_product_subcategory_fpd
SELECT
    campaign_product_subcategory_id,
    campaign_id,
    subcategory_id,
    discount
FROM
    ods.ods_campaign_product_subcategory_fpd;
    
SELECT * FROM dwd.dwd_campaign_product_subcategory_fpd_compat LIMIT 10;
"""