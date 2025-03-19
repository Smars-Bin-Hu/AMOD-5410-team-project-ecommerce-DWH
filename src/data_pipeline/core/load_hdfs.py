
"""
load_hdfs.py

This Module: ..
"""
from pyspark.sql.functions import current_date, date_format, col
from .parse_field_type import parse_field_type
from data_pipeline.utils import logger

def load_hdfs(table:dict, df) -> bool:
    # check Hive ODS Layer HDFS target path
    # hive_ods_hdfs_path = HadoopEnvConfig.get_hive_ods_hdfs_path()
    # if not HDFSUtils.check_hdfs_path(hive_ods_hdfs_path):
    #     logger.smars_dev(f"HDFS path {hive_ods_hdfs_path} Not found")
    #     return False

    """Load data to HDFS"""
    # read table configuration information
    hive_hdfs_table_path = table["hive_hdfs_table_path"]
    save_mode = table["save_mode"]
    hive_format = table["hive_format"]
    partition_field = table["partition_field"] # None or data_date
    field_casting_map = table["field_casting_map"]
    avro_schema_json = table["avro_schema_json"]

    # load the dataframe to hive
    try:
        # field rename and casting data type
        for key, value in field_casting_map.items():
            # 假设上游列是大写 => uppercase
            # rename e.g. "CUSTOMERPRODUCTRATING_ID" -> "customerproductrating_id"
            df = df.withColumnRenamed(key.upper(), key)

            # 再 cast
            df = df.withColumn(key, col(key).cast(parse_field_type(value)))

        # add partition field if the table has partition
        if partition_field == "data_date":
            df = df.withColumn("data_date", date_format(current_date(), "yyyy-MM-dd")) # add new column filled with current_date()

        # write df to hive
        if partition_field == "None":
            (
                df.write
                .format(hive_format)
                .mode(save_mode)
                .option("avroSchema", avro_schema_json)
                .option("compression", "uncompressed") # do not use Snappy
                .save(hive_hdfs_table_path)
            )
        else:
            # has partition field
            (
                df.write
                .format(hive_format)
                .mode(save_mode)
                .option("avroSchema", avro_schema_json)
                .option("compression", "uncompressed") # do not use Snappy
                .partitionBy(partition_field)
                .save(hive_hdfs_table_path)
            )

        logger.smars_dev(f"Successfully saved DataFrame ({save_mode}) to HDFS path '{hive_hdfs_table_path}' in {hive_format} format.")
        return True
    except Exception as e:
        logger.error(f"Failed to save DataFrame to HDFS path '{hive_hdfs_table_path}': {e}")
        return False