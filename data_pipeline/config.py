"""
config.py

Config Files, including Database, HDFS constant variable info

"""

class Config:
    """
        Configuration Info Class
        includes the configuration to database, HDFS,etc...
    """

    # Hadoop Cluster & HDFS
    HADOOP_HOST="hadoop-master"
    HADOOP_USER="root" # authenticate without password using ssh-keygen and send the pub key to hadoop cluster
    HDFS_PATH = "/user/hdfs/oracle_data"

    # Oracle Database Configuration
    ORACLE_JDBC_DRIVER_PATH = "/opt/sqoop/lib/ojdbc8.jar"
    ORACLE_HOST = "oracle-oltp"
    ORACLE_PORT = "1521"
    ORACLE_SERVICE_NAME = "ORCLPDB1"
    ORACLE_USERNAME = "Smars"
    ORACLE_PASSWORD = "Whos3301919!"
    ORACLE_DRIVER = "oracle.jdbc.OracleDriver"

    # Spark
    SPARK_APP_NAME = "OracleToHDFS"
    SPARK_JDBC_DRIVER_PATH = "/opt/spark/jars/ojdbc8.jar"

    # Logging files path
    LOG_FILE = "logs/etl_process.log"

    class OracleTable:
        ORACLE_TABLE = {

        }