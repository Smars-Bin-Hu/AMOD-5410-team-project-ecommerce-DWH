
"""
load_ck.py

This Module: ..
"""
from data_pipeline.utils import logger

def load_to_ck(clickhouse_database:str, clickhouse_table:str, dataframe) -> bool:
    try:
        logger.smars_dev(f"Load data frame to clickhouse {clickhouse_database}.{clickhouse_table} ")
        dataframe.writeTo(f"clickhouse.{clickhouse_database}.{clickhouse_table}").append()
        return True
    except Exception as e:
        logger.smars_dev(f"Error processing table {clickhouse_table}: {e}")
        return False