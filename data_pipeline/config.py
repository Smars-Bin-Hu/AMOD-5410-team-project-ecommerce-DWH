"""
config.py

Config Files, including Database, HDFS constant variable info
"""

class OracleDBConfig:
    # Oracle Database Configuration
    ORACLE_JDBC_DRIVER_PATH = "/opt/spark/jars/ojdbc8.jar"
    ORACLE_HOST = "oracle-oltp"
    ORACLE_PORT = "1521"
    ORACLE_SERVICE_NAME = "ORCLPDB1"
    ORACLE_USERNAME = "Smars"
    ORACLE_PASSWORD = "Whos3301919!"
    ORACLE_DRIVER = "oracle.jdbc.OracleDriver"
    ORACLE_JDBC_URL = f"jdbc:oracle:thin:@//{ORACLE_HOST}:{ORACLE_PORT}/{ORACLE_SERVICE_NAME}"

class HadoopConfig:
    HADOOP_HOST="hadoop-master"
    HADOOP_USER="root" # authenticate without password using ssh-keygen and send the pub key to hadoop cluster
    HDFS_PATH = "/tmp/root/"

class SparkConfig:
    SPARK_APP_NAME = "OracleToHDFS"

class LoggingConfig:
    SMARS_DEV_LOG_LEVEL= 25 # INFO = 20, WARNING = 30
    SMARS_DEV_LOG_LEVEL_NAME = "SMARS_DEV"
    LOG_FILE = "logs/etl_process.log"

class Config:
    """
        Configuration Info Class
        includes the configuration to database, HDFS,etc...
    """
    SparkConfig = SparkConfig
    HadoopConfig = HadoopConfig
    OracleDBConfig = OracleDBConfig
    LoggingConfig = LoggingConfig