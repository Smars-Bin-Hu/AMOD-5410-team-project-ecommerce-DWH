"""
etl_oracle_to_hdfs.py

This Module: define OracleToHDFS class, to extract the data from Oracle and load to the HDFS
"""

from data_pipeline import spark
from data_pipeline.configs import LoggingConfig
from data_pipeline.utils import LoggingUtils

# create a logger for current etl
smars_dev_log_level = int(LoggingConfig.get_smars_dev_log_level())
smars_dev_log_level_name = LoggingConfig.get_smars_dev_log_level_name()
logger = LoggingUtils.setup_custom_logger(
    "ETL_ORACLE_TO_HDFS_LOGGER",
    smars_dev_log_level,
    smars_dev_log_level_name
)

class ETLOracleToHDFS:
    """ETL Job Class: Oracle Data Extract and Load to HDFS"""

    @staticmethod
    def extract(table:dict, oracle_config:dict):
        """extract 1 table from Oracle"""
        oracle_table_name = table.oracle_table_name
        oracle_table_sql_query = table.table_sql_query

        # get the configuration info to oracle DB
        oracle_jdbc_url = oracle_config["oracle_jdbc_url"]
        properties = oracle_config["properties"]

        try:
            # Attempt to read the table
            logger.smars_dev(f"Read Oracle Table: {oracle_table_name}")
            df = spark.read.jdbc(
                url=oracle_jdbc_url,
                table=oracle_table_sql_query,
                properties=properties
            )

            # Check if the DataFrame is empty (no rows)
            if df.head(1):
                logger.smars_dev(f"Successfully extract data from table: {oracle_table_name}")
            else:
                logger.smars_dev(f"Table '{oracle_table_name}' is empty.")
        except Exception as e:
            # Log if an error occurs (e.g., table does not exist)
            logger.error(f"Failed to read table '{oracle_table_name}': {e}")

        return df

    @staticmethod
    def load(df, hdfs_path:dict):
        """Load data to HDFS"""
        try:
            df.write\
                .format("avro")\
                .mode("overwrite")\
                .save(hdfs_path)
            logger.smars_dev(f"Successfully saved DataFrame to HDFS path '{hdfs_path}' in Avro format.")
        except Exception as e:
            logger.error(f"Failed to save DataFrame to HDFS path '{hdfs_path}': {e}")

    @staticmethod
    def run(self, table_name):
        """execute the entire ETL job"""
        logger.smars_dev(f"Processing Table Name: {table_name}")

        # 1. Extract the data
        df = self.extract(table_name)

        # 2. Load the data
        ETLOracleToHDFS.load(df_transformed)

        logger.smars_dev("ETL job task complete！")

    def stop():
        """stop SparkSession"""
        logger.smars_dev("Stopping SparkSession...")
        spark.stop()
