from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("OracleExtractionByPySpark") \
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
    else:
        print(f"Table '{oracle_table_name}' is empty.")
except Exception as e:
    # Log if an error occurs (e.g., table does not exist)
    print(f"Failed to read table '{oracle_table_name}': {e}")