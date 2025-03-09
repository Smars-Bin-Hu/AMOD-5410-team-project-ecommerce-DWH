import json
from pathlib import Path
from data_pipeline.configs import (
    LoggingConfig,
    DatabaseConnectionConfig,
    HadoopEnvConfig,
    etl_tables_config
)
from data_pipeline.utils import (
    LoggingUtils,
    OracleDatabaseUtils,
    HDFSUtils,
)
from data_pipeline.core import (
    extract,
    load,
)

# create a logger for current util
smars_dev_log_level = int(LoggingConfig.get_smars_dev_log_level())
smars_dev_log_level_name = LoggingConfig.get_smars_dev_log_level_name()
logger = LoggingUtils.setup_custom_logger(
    "ETL_MAIN_LOGGER",
    smars_dev_log_level,
    smars_dev_log_level_name
)

# record the result of extract and load tables
# NOTE: only load the successful and
successful_extract_tables = []
empty_tables = []
failed_extract_tables = []
successful_load_tables = []
failed_load_tables = []

# Connect Oracle
oracle_db_config = DatabaseConnectionConfig("oracle","1")

# Read the ETL tables config JSON
def spark_etl(spark) -> bool:
    # 1. test Oracle connection
    # create oracle connection configuration instance
    if not OracleDatabaseUtils.test_oracle_connection(oracle_db_config):
        logger.smars_dev("Terminal the job：Oracle failed to connect")
        return False

    # 2. check Hive ODS Layer HDFS target path
    hive_ods_hdfs_path = HadoopEnvConfig.get_hive_ods_hdfs_path()
    if not HDFSUtils.check_hdfs_path(hive_ods_hdfs_path):
        logger.smars_dev(f"HDFS path {hive_ods_hdfs_path} Not found")
        return False

    # 3. do the etl jobs
    for table in etl_tables_config:
        try:
            logger.smars_dev(f"Starting ETL for table: {table['oracle_table_name']}")

            # Step 1: Extract Data from Oracle
            df = extract(spark, table, oracle_db_config)

            if df.schema is None:  # Case 3: Extraction failed
                failed_extract_tables.append(table["oracle_table_name"])
                logger.smars_dev(f"Failed to extract data from table: {table['oracle_table_name']}")
                continue  # Skip load step

            successful_extract_tables.append(table["oracle_table_name"])

            if df.isEmpty():  # Case 2: Table exists, but has no data
                empty_tables.append(table["oracle_table_name"])
                logger.smars_dev(f"Table {table['oracle_table_name']} is empty. Skipping load.")
                continue  # Skip load step

            # Step 2: Load Data into HDFS
            success = load(table, df)

            if success:
                successful_load_tables.append(table["oracle_table_name"])
                logger.smars_dev(f"Successfully loaded table: {table['oracle_table_name']}")
            else:
                failed_load_tables.append(table["oracle_table_name"])
                logger.smars_dev(f"Failed to load table: {table['oracle_table_name']}")

        except Exception as e:
            failed_extract_tables.append(table["oracle_table_name"])
            logger.smars_dev(f"Error processing table {table['oracle_table_name']}: {e}")

    logger.smars_dev("=== ETL jobs finished ===")
    logger.smars_dev(f"Successfully Extracted: {successful_extract_tables}")
    logger.smars_dev(f"Failed to Extract: {failed_extract_tables}")
    logger.smars_dev(f"Failed to Extract: {empty_tables}")
    logger.smars_dev(f"Successfully Loaded: {successful_load_tables}")
    logger.smars_dev(f"Failed to Load: {failed_load_tables}")
    return True