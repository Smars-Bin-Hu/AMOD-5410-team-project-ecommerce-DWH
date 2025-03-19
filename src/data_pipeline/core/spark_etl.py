from data_pipeline.configs import (
    DatabaseConnectionConfig,
    etl_tables_config
)
from data_pipeline.utils import (
    OracleDatabaseUtils,
    logger
)
from .extract_oracle import extract_oracle
from .load_hdfs import load_hdfs

# record the result of extract and load tables
# NOTE: only load the successful and
successful_extract_tables = []
empty_tables = []
failed_extract_tables = []
successful_load_tables = []
failed_load_tables = []

# Get Database Configuration: Oracle, Instance 1
oracle_db_config = DatabaseConnectionConfig("oracle","1")

# Read the ETL tables config JSON
def spark_etl(spark) -> bool:
    # 1. test Oracle connection: Oracle Instance 1
    if not OracleDatabaseUtils.test_oracle_connection(oracle_db_config,"oracle","1"):
        logger.smars_dev("Terminal the job：Oracle failed to connect")
        return False

    # 2. check Hive ODS Layer HDFS target path
    # hive_ods_hdfs_path = HadoopEnvConfig.get_hive_ods_hdfs_path()
    # if not HDFSUtils.check_hdfs_path(hive_ods_hdfs_path):
    #     logger.smars_dev(f"HDFS path {hive_ods_hdfs_path} Not found")
    #     return False

    # 3. do the etl jobs
    for table in etl_tables_config:
        try:
            logger.smars_dev(f"Starting ETL for table: {table['oracle_table_name']}")

            # Step 1: Extract Data from Oracle
            df = extract_oracle(spark, table, oracle_db_config)

            if df.schema is None:  # Case 3: Extraction failed
                failed_extract_tables.append(table["oracle_table_name"])
                logger.smars_dev(f"Failed to extract data from table: {table['oracle_table_name']} because df.schema is None")
                continue  # Skip load step

            successful_extract_tables.append(table["oracle_table_name"])

            if df.isEmpty():  # Case 2: Table exists, but has no data
                empty_tables.append(table["oracle_table_name"])
                logger.smars_dev(f"Table {table['oracle_table_name']} is empty. Skipping load.")
                continue  # Skip load step

            # Step 2: Load Data into HDFS
            success = load_hdfs(table, df)

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
    logger.smars_dev(f"Empty tables: {empty_tables}")
    logger.smars_dev(f"Successfully Loaded: {successful_load_tables}")
    logger.smars_dev(f"Failed to Load: {failed_load_tables}")
    return True