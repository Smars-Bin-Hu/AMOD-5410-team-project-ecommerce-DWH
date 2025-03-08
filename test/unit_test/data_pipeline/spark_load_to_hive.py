import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format, current_date
from pyspark.sql.types import IntegerType, StringType

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
oracle_table_name = "CATEGORY"
oracle_table_sql_query = f"SELECT * FROM CATEGORY"

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
            df.show()
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

hive_hdfs_table_path = "/user/hive/warehouse/ods/ods_category_fpd"
save_mode = "overwrite"
hive_format = "avro"
avro_schema_json = """
{
  "type": "record",
  "name": "category",
  "namespace": "com.ods.avro",
  "fields": [
    {
      "name": "category_id",
      "type": "int",
      "doc": "Unique identifier for table category"
    },
    {
      "name": "category_name",
      "type": "string",
      "doc": "Name of category, like Clothing, Books, Grocery..."
    }
  ]
}
"""
# load
try:
    df = df.withColumn("DATA_DATE", date_format(current_date(), "yyyy-MM-dd"))
    # 2) 如果你的 DataFrame 中列是 `CATEGORY_ID` 等，需要先转换为匹配的类型 & 字段名
    df = df.withColumnRenamed("CATEGORY_ID", "category_id") \
        .withColumnRenamed("CATEGORY_NAME", "category_name")
    df = df.withColumn("category_id", col("category_id").cast(IntegerType()))
    df = df.withColumn("category_name", col("category_name").cast(StringType()))

    # 3) 添加分区列
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