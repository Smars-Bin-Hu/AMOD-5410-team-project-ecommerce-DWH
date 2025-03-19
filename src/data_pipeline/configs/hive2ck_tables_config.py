hive2ck_tables_configs = [
    {
        "hive_db" : "dws",
        "tables" : [
            {
                "ck_db" :"ads_data_mart_ecomerce",
                "ck_table" : "ads_orders_detailed_info_wide_ipd",
                "hive_table" : "dws_orders_detailed_info_wide_ipd",
                "hive_table_partition_field" : "data_date"
            }
        ]
    },{
        "hive_db" : "dwt",
        "tables" : [
            {
                "ck_db" :"ads_data_mart_ecomerce",
                "ck_table" : "ads_orders_detailed_info_wide_ipd",
                "hive_table" : "dws_orders_detailed_info_wide_ipd",
                "hive_table_partition_field" : "data_date",
            }
        ]
    }
]
