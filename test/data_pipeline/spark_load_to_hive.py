import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format, current_date
from pyspark.sql.types import IntegerType, StringType, DecimalType

spark = SparkSession.builder \
    .appName("OracleExtractionByPySpark") \
    .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.3.0")\
    .getOrCreate()

# get the configuration info to oracle DB
ORACLE_HOST = "oracle-oltp"
ORACLE_PORT = "1521"
ORACLE_SERVICE_NAME = "ORCLPDB1"
ORACLE_USERNAME = "Smars"
ORACLE_PASSWORD = "Whos3301919!"
oracle_jdbc_url = f"jdbc:oracle:thin:@//{ORACLE_HOST}:{ORACLE_PORT}/{ORACLE_SERVICE_NAME}"
properties =  {
    "user": ORACLE_USERNAME,
    "password": ORACLE_PASSWORD,
    "driver": "oracle.jdbc.OracleDriver"
}
oracle_table_name = "CUSTOMER_PRODUCT_RATINGS"
oracle_table_sql_query = f"SELECT * FROM CUSTOMER_PRODUCT_RATINGS"

def extract(oracle_table_name, oracle_jdbc_url, oracle_table_sql_query, properties):
    try:
        # Attempt to read the table
        print(f"Read Oracle Table: {oracle_table_name}")
        df = spark.read \
            .format("jdbc") \
            .option("url", oracle_jdbc_url) \
            .option("query", oracle_table_sql_query) \
            .options(**properties) \
            .load()

        # Check if the DataFrame is empty (no rows)
        if df.head(1):
            # df.show()
            print(f"Successfully extract data from table: {oracle_table_name}")
            return df
        else:
            print(f"Table '{oracle_table_name}' is empty.")
            return spark.createDataFrame([], schema=df.schema)
    except Exception as e:
        # Log if an error occurs (e.g., table does not exist)
        print(f"Failed to read table '{oracle_table_name}': {e}")
        return spark.createDataFrame([], schema=None)

df = extract(oracle_table_name, oracle_jdbc_url, oracle_table_sql_query, properties)

hive_hdfs_table_path = "/user/hive/warehouse/ods/ods_customer_product_ratings_ipd"
save_mode = "overwrite"
hive_format = "avro"
avro_schema_json = """
{
  "type": "record",
  "name": "customer_product_ratings",
  "namespace": "com.ods.avro",
  "fields": [
    {
      "name": "customerproductrating_id",
      "type": "int",
      "doc": "Unique id for each row in table customer_product_ratings"
    },
    {
      "name": "customer_id",
      "type": "int",
      "doc": "The customer gave the review and ratings"
    },
    {
      "name": "product_id",
      "type": "int",
      "doc": "The product that was given the review and ratings"
    },
    {
      "name": "ratings",
      "type": {
        "type": "bytes",
        "logicalType": "decimal",
        "precision": 2,
        "scale": 1
      },
      "doc": "The ratings specific number"
    },
    {
      "name": "review",
      "type": [
        "null",
        "string"
      ],
      "default": null,
      "doc": "The review text"
    },
    {
      "name": "sentiment",
      "type": [
        "null",
        "string"
      ],
      "default": null,
      "doc": "The final sentiment ('good' or 'bad')"
    }
  ]
}
"""
# load
try:
    df = df.withColumnRenamed("customerproductrating_id".upper(), "customerproductrating_id") \
        .withColumnRenamed("customer_id".upper(), "customer_id")\
        .withColumnRenamed("product_id".upper(), "product_id")\
        .withColumnRenamed("ratings".upper(), "ratings")\
        .withColumnRenamed("review".upper(), "review")\
        .withColumnRenamed("sentiment".upper(), "sentiment")\

    df = df.withColumn("customerproductrating_id", col("customerproductrating_id").cast(IntegerType()))
    df = df.withColumn("customer_id", col("customer_id").cast(IntegerType()))
    df = df.withColumn("product_id", col("product_id").cast(IntegerType()))
    df = df.withColumn("ratings", col("ratings").cast(DecimalType(2, 1)))
    df = df.withColumn("review", col("review").cast(StringType()))
    df = df.withColumn("sentiment", col("sentiment").cast(StringType()))

    df = df.withColumn("data_date", date_format(current_date(), "yyyy-MM-dd"))

    (
        df.write
        .format(hive_format)  # "avro"
        .mode(save_mode)  # "overwrite"
        .option("avroSchema", avro_schema_json)
        .option("compression", "uncompressed") # do not use Snappy
        .partitionBy("data_date")
        .save(hive_hdfs_table_path)
    )

    print(f"Successfully saved DataFrame ({save_mode}) to HDFS path '{hive_hdfs_table_path}' in {hive_format} format.")
except Exception as e:
    print(f"Failed to save DataFrame to HDFS path '{hive_hdfs_table_path}': {e}")