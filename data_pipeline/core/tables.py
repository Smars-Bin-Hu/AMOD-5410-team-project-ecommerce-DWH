"""
    All Full Load Tables on the Oracle DB and map to Hive
"""
# Define table parameters as a structured list for easier iteration and processing
tables = [
    {
        "oracle_table_name": "CATEGORY",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_category_fpd",
        "hive_format": "avro",
        "save_mode": "overwrite",
        "oracle_table_sql_query" : f"SELECT * FROM CATEGORY"
    },
    {
        "oracle_table_name": "ORDERS",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_orders_ipd",
        "hive_format": "avro",
        "save_mode": "append",
        "oracle_table_sql_query" : f"select count(*) from ORDERS where ORDER_DATE = date'2021-01-16'"
    },
]
