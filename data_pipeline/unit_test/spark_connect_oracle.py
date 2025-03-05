from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
    .appName("OracleConnectionTest") \
    .getOrCreate()

# Oracle DB Configuration
ORACLE_HOST = "oracle-oltp"
ORACLE_PORT = "1521"
ORACLE_SERVICE_NAME = "ORCLPDB1"
ORACLE_USERNAME = "Smars"
ORACLE_PASSWORD = "Whos3301919!"
ORACLE_JDBC_URL = f"jdbc:oracle:thin:@//{ORACLE_HOST}:{ORACLE_PORT}/{ORACLE_SERVICE_NAME}"
properties = {
    "user": ORACLE_USERNAME,
    "password": ORACLE_PASSWORD,
    "driver": "oracle.jdbc.OracleDriver"
}

# choose the table as parameter
table_name = "DUAL"  # oracle must have this table

try:
    # read Oracle data
    df = spark.read.jdbc(url=ORACLE_JDBC_URL, table=table_name, properties=properties)

    # print the data
    print("Oracle connected successfully！")
    df.show()

except Exception as e:
    print("Oracle failed to connect:", str(e))

finally:
    # stop SparkSession
    spark.stop()
