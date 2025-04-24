from batch_processing.utils import read_sql, logger, sql_render_partition_date
from batch_processing.configs import sql_dml_files_dwm

def dwd_to_dwm(spark, table_name, partition_data) -> bool:
    logger.smars_dev(f"Data processing - DWD to DWM - table name: {table_name} is executing")

    try:
        # Get the DML SQL files Path for DWD Layer
        path_to_dml_sql = sql_dml_files_dwm.get(table_name).get("path")
        tbl_has_partition = sql_dml_files_dwm.get(table_name).get("has_partition")

        # get the raw sql
        raw_sql = read_sql(path_to_dml_sql)

        # replace the partition field with the data
        if tbl_has_partition and partition_data is not None:
            sql = sql_render_partition_date(
                raw_sql,
                partition_data,
                placeholder="${data_date}"
            )
        else:
            sql = raw_sql

        # execute sql
        spark.sql(sql)
        logger.smars_dev(f"Data processing - DWD to DWM - table name: {table_name} is finished")
    except Exception as e:
        logger.smars_dev(f"Data processing - DWD to DWM - table name: {table_name} is failed. Exception Info: {e}")
        return False

    # output the logs
    return True