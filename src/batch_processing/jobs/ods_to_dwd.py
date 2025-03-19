from .batch_processing.utils import read_sql, logger
from .batch_processing.configs import sql_dml_files_path_dwd

def ods_to_dwd(spark) -> bool:
    successful_tables = []
    failed_tables = []

    # Get the DML SQL files Path for DWD Layer
    for key, value in sql_dml_files_path_dwd.items():
        logger.smars_dev(f"Data processing - ODS to DWD - table name: {key} is executing")
        try:
            sql = read_sql(value)
            spark.sql(sql)   # execute sql
            logger.smars_dev(f"Data processing - ODS to DWD - table name: {key} is finished")
            successful_tables.append(key)
        except Exception as e:
            logger.smars_dev(f"Data processing - ODS to DWD - table name: {key} is failed. Exception Info: {e}")
            failed_tables.append(key)

    # output the logs
    logger.smars_dev("=== ODS to DWD Transformation jobs finished ===")
    logger.smars_dev(f"Successfully Extracted: {successful_tables}")
    logger.smars_dev(f"Failed to Extract: {failed_tables}")
    return True