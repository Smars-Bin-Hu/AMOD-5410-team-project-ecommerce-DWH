from .batch_processing.utils import read_sql, logger
from .batch_processing.configs import sql_dml_files_path_dwd

def ods_to_dwd(spark, table_name, partition_field, data_date) -> bool:
    logger.smars_dev(f"Data processing - ODS to DWD - table name: {table_name} is executing")

    try:
        # Get the DML SQL files Path for DWD Layer
        path_to_dml_sql = sql_dml_files_path_dwd.get(table_name)

        # get the raw sql
        raw_sql = read_sql(path_to_dml_sql)

        # replace the partition field with the data


        spark.sql(sql)   # execute sql
        logger.smars_dev(f"Data processing - ODS to DWD - table name: {table_name} is finished")
    except Exception as e:
        logger.smars_dev(f"Data processing - ODS to DWD - table name: {table_name} is failed. Exception Info: {e}")

    # output the logs
    return True