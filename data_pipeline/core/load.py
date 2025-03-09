
"""
load.py

This Module: ..
"""
from pyspark.sql.functions import  current_date, date_format, col
from .parse_avro_field_type import parse_avro_type
from data_pipeline.configs import LoggingConfig
from data_pipeline.utils import LoggingUtils

# create a logger for current etl
smars_dev_log_level = int(LoggingConfig.get_smars_dev_log_level())
smars_dev_log_level_name = LoggingConfig.get_smars_dev_log_level_name()
logger = LoggingUtils.setup_custom_logger(
    "LOAD_LOGGER",
    smars_dev_log_level,
    smars_dev_log_level_name
)
def load(table:dict, df) -> bool:
    """Load data to HDFS"""
    # read table configuration information
    hive_hdfs_table_path = table["hive_hdfs_table_path"]
    save_mode = table["save_mode"]
    hive_format = table["hive_format"]
    partition_field = table["partition_field"] # None or data_date
    avro_schema_json = table["avro_schema_json"]
    avro_schema_table_fields : list = avro_schema_json["fields"]

    # load the dataframe to hive
    try:
        # field rename and casting data type
        for field_def in avro_schema_table_fields:
            field_name = field_def["name"]  # e.g. "customerproductrating_id"
            spark_type = parse_avro_type(field_def["type"])

            # 假设上游列是大写 => uppercase
            # rename e.g. "CUSTOMERPRODUCTRATING_ID" -> "customerproductrating_id"
            df = df.withColumnRenamed(field_name.upper(), field_name)

            # 再 cast
            df = df.withColumn(field_name, col(field_name).cast(spark_type))

        # add partition field if the table has partition
        if partition_field == "data_date":
            df = df.withColumn("data_date", date_format(current_date(), "yyyy-MM-dd")) # add new column filled with current_date()

        # write df to hive
        if partition_field == "None":
            (
                df.write
                .format(hive_format)
                .mode(save_mode)
                .save(hive_hdfs_table_path)
            )
        else:
            # has partition field
            (
                df.write
                .format(hive_format)
                .mode(save_mode)
                .partitionBy(partition_field)
                .save(hive_hdfs_table_path)
            )

        logger.smars_dev(f"Successfully saved DataFrame ({save_mode}) to HDFS path '{hive_hdfs_table_path}' in {hive_format} format.")
        return True
    except Exception as e:
        logger.error(f"Failed to save DataFrame to HDFS path '{hive_hdfs_table_path}': {e}")
        return False