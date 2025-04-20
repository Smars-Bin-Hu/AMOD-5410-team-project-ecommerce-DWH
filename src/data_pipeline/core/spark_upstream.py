from data_pipeline.configs import (
    DatabaseConnectionConfig,
    oracle2hive_tables_config
)
from data_pipeline.utils import (
    OracleDatabaseUtils,
    logger
)
from .extract_oracle import extract_oracle
from .load_hdfs import load_hdfs

# record the result of extract and load tables
# NOTE: only load the successful extract tables
successful_extract_tables = []
empty_tables = []
failed_extract_tables = []
successful_load_tables = []
failed_load_tables = []

# Read the ETL tables config JSON
def spark_upstream(
        spark,
        oltp_data_source : dict,
        dwh_data_target : dict,
        partition_data : str
) -> bool:
    # get target OLTP Database Configuration
    db_type = oltp_data_source.get("db_type")
    instance_code = oltp_data_source.get("instance_code")
    db_conn_config = DatabaseConnectionConfig(db_type, instance_code)

    # get target DWH Configuration and confirm the data load job main function
    dwh_type = dwh_data_target.get("dwh_type")
    load_job_main_func = {
        "hive" : load_hdfs,
    }
    load_job_main_func = load_job_main_func.get(dwh_type, "hive")

    # Extract data based on OLTP Type
    if db_type == "oracle":
        # 1. test OLTP connection
        if not OracleDatabaseUtils.test_oracle_connection(db_conn_config,db_type,instance_code):
            logger.smars_dev("Terminal the job：Oracle failed to connect")
            return False

        # 2. do the etl jobs
        for table in oracle2hive_tables_config:
            try:
                logger.smars_dev(f"Starting ETL for table: {table['oracle_table_name']}")

                # Step 1: Extract Data from Oracle
                df = extract_oracle(spark, table, db_conn_config)

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
                success = load_job_main_func(table, df, partition_data)

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
    # elif db_type == "mysql":
    else:
        logger.smars_dev(f"DB TYPE INVALID : {db_type} CANNOT FOUND ")
        return False