"""
etl_oracle_to_hdfs.py

This Module: define OracleToHDFS class, to extract the data from Oracle and load to the HDFS
"""

from data_pipeline import spark
from pyspark.sql.functions import lit, current_date, date_format
from data_pipeline.configs import LoggingConfig\
    ,DatabaseConnectionConfig
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
    def extract(table, oracle_config):
        """extract 1 table from Oracle"""
        oracle_table_name = table["oracle_table_name"]
        oracle_table_sql_query = table["oracle_table_sql_query"]

        # get the configuration info to oracle DB
        oracle_jdbc_url = oracle_config.get_jdbc_url()
        properties = oracle_config.get_properties()

        try:
            # Attempt to read the table
            logger.smars_dev(f"Read Oracle Table: {oracle_table_name}")
            df = spark.read\
                .format("jdbc") \
                .option("url", oracle_jdbc_url) \
                .option("query", oracle_table_sql_query) \
                .options(**properties) \
                .load()

            # Check if the DataFrame is empty (no rows)
            if df.head(1):
                logger.smars_dev(f"Successfully extract data from table: {oracle_table_name}")
                return df
            else:
                logger.smars_dev(f"Table '{oracle_table_name}' is empty.")
                return spark.createDataFrame([], schema=df.schema)
        except Exception as e:
            # Log if an error occurs (e.g., table does not exist)
            logger.error(f"Failed to read table '{oracle_table_name}': {e}")
            return spark.createDataFrame([], schema=None)

    @staticmethod
    def load(table:dict, df):
        """Load data to HDFS"""
        # read table configuration information
        hive_hdfs_table_path = table["hive_hdfs_table_path"]
        save_mode = table["save_mode"]
        hive_format = table["hive_format"]
        partition_field = table["partition_field"]

        # load the dataframe to hive
        try:
            # partition field
            df = df.withColumn("DATA_DATE", date_format(current_date(), "yyyy-MM-dd")) # add new column filled with current_date()

            # write df to hive
            (
                df.write
                .format(hive_format)
                .mode(save_mode)
                .partitionBy(partition_field)
                .save(hive_hdfs_table_path)
            )
            logger.smars_dev(f"Successfully saved DataFrame ({save_mode}) to HDFS path '{hive_hdfs_table_path}' in {hive_format} format.")
        except Exception as e:
            logger.error(f"Failed to save DataFrame to HDFS path '{hive_hdfs_table_path}': {e}")

    # @staticmethod
    # def run(self, table_name):
    #     """execute the entire ETL job"""
    #     logger.smars_dev(f"Processing Table Name: {table_name}")
    #
    #     # 1. Extract the data
    #     df = self.extract(table_name)
    #
    #     # 2. Load the data
    #     ETLOracleToHDFS.load(df_transformed)
    #
    #     logger.smars_dev("ETL job task complete！")
    #
    # def stop():
    #     """stop SparkSession"""
    #     logger.smars_dev("Stopping SparkSession...")
    #     spark.stop()