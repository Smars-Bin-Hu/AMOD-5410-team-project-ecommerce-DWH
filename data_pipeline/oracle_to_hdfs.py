"""
oracle_to_hdfs.py

This Module: define OracleToHDFS class, to extract the data from Oracle and load to the HDFS
"""

from pyspark.sql import SparkSession
from config import Config # Config.py

# Utils.py
from utils import LoggingUtils

class OracleToHDFS:
    """ETL Job Class: Oracle Data Extract and Load to HDFS"""

    def __init__(self):
        """
            Constructor:
                initialize SparkSession and Global Logging System
         """

        # launch the Logging System
        self.logger = LoggingUtils.setup_custom_logger(
            "ORACLE_TO_HDFS",
            Config.LoggingConfig.SMARS_DEV_LOG_LEVEL,
            Config.LoggingConfig.SMARS_DEV_LOG_LEVEL_NAME
        )
        self.logger.info("Initializing SparkSession...")

        # launch the SparkSession
        self.spark = SparkSession.builder \
            .appName(Config.SPARK_APP_NAME) \
            .getOrCreate()

    def extract(self, table_name):
        """extract 1 table from Oracle"""
        self.logger.info(f"Read Oracle Table: {table_name}")

        # config the user information
        properties = {
            "user": Config.ORACLE_USER,
            "password": Config.ORACLE_PASSWORD,
            "driver": Config.ORACLE_DRIVER
        }

        # connect Oracle using Service Name instead of SID
        ORACLE_JDBC_URL = f"jdbc:oracle:thin:@//{Config.ORACLE_HOST}:{Config.ORACLE_PORT}/{Config.ORACLE_SERVICE_NAME}"

        # get the table
        df = self.spark.read.jdbc(url=ORACLE_JDBC_URL, table=table_name, properties=properties)

        return df

    def load(self, df):
        """Load data to HDFS"""
        self.logger.info(f"Loading tables to HDFS: {Config.HDFS_PATH}")
        df.write\
            .mode("overwrite")\
            .parquet(Config.HDFS_PATH)

    def run(self, table_name):
        """execute the entire ETL job"""
        self.logger.info(f"Processing Table Name: {table_name}")

        # 1. Extract the data
        df = self.extract(table_name)

        # 2. Load the data
        self.load(df_transformed)

        self.logger.info("ETL job task complete！")

    def stop(self):
        """stop SparkSession"""
        self.logger.info("Stopping SparkSession...")
        self.spark.stop()
