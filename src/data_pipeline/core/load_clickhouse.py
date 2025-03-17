from pyspark.sql import SparkSession
import clickhouse_connect

spark = SparkSession.builder \
    .appName("HiveToClickHouse") \
    .enableHiveSupport() \
    .getOrCreate()

# 读取 Hive Parquet 数据
df = spark.read.format("parquet").load("hdfs://path_to_hive_table/dwd_orders")

client = clickhouse_connect.get_client(
    host='vm9roqk7je.westus3.azure.clickhouse.cloud',
    user='default',
    password='8h2Dpa6Y_pl07',
    secure=True
)

print("Result:", client.query("SELECT 1").result_set[0][0])

# ClickHouse JDBC 配置
clickhouse_url = "jdbc:clickhouse://vm9roqk7je.westus3.azure.clickhouse.cloud:8443"
clickhouse_properties = {
    "user": "default",
    "password": "8h2Dpa6Y_pl07",
    "driver": "ru.yandex.clickhouse.ClickHouseDriver"
}

# 写入 ClickHouse
df.write \
    .format("jdbc") \
    .option("url", clickhouse_url) \
    .option("dbtable", "dwd_orders") \
    .option("user", "default") \
    .option("password", "") \
    .option("batchsize", "100000") \
    .option("isolationLevel", "NONE") \
    .option("numPartitions", "4") \
    .mode("append") \
    .save()
