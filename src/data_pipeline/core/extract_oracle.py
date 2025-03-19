"""
extract_oracle.py

This Module: define OracleToHDFS class, to extract the data from Oracle and load to the HDFS
"""
from pyspark.sql import DataFrame
from data_pipeline.utils import logger

def extract_oracle(spark, table, oracle_config) -> DataFrame:
    """extract 1 table from Oracle"""
    oracle_table_name = table["oracle_table_name"]
    oracle_table_sql_query = table["oracle_table_sql_query"]

    # get the configuration info to oracle DB
    oracle_jdbc_url = oracle_config.get_jdbc_url("oracle","1")
    properties = oracle_config.get_properties("oracle","1")

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
            df.show()
            return df
        else:
            logger.smars_dev(f"Table '{oracle_table_name}' is empty.")
            return spark.createDataFrame([], schema=df.schema)
    except Exception as e:
        # Log if an error occurs (e.g., table does not exist)
        logger.error(f"Failed to read table '{oracle_table_name}': {e}")
        return spark.createDataFrame([], schema=None)


