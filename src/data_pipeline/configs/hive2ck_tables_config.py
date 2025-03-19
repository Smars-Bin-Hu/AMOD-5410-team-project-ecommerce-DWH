hive2ck_tables_configs = [
    {
        "ck_db" :"ads_data_mart_ecomerce",
        "ck_table" : "ads_orders_detailed_info_wide_ipd",
        "hive_db" : "dws",
        "hive_table" : "dws_orders_detailed_info_wide_ipd",
        "hive_table_partition_field" : "data_date",
        "load_data_partition_data" : "2025-03-10"
    }
]
