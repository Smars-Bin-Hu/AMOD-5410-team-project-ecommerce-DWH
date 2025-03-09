
etl_tables_config = [
    {
        "oracle_table_name": "CAMPAIGN_PRODUCT_SUBCATEGORY",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_campaign_product_subcategory_fpd",
        "hive_format": "avro",
        "save_mode": "overwrite",
        "oracle_table_sql_query" : f"select * from CAMPAIGN_PRODUCT_SUBCATEGORY",
        "partition_field" : "None",
        "avro_schema_json" : {
            "type": "record",
            "name": "campaign_product_subcategory",
            "namespace": "com.ods.avro",
            "fields": [
                {
                    "name": "campaign_product_subcategory_id",
                    "type": "int",
                    "doc": "Unique id for each row in table campaign_product_subcategory"
                },
                {
                    "name": "campaign_id",
                    "type": "int",
                    "doc": "Campaign id (16 in total)"
                },
                {
                    "name": "subcategory_id",
                    "type": "int",
                    "doc": "Subcategory id (100 in total)"
                },
                {
                    "name": "discount",
                    "type": {
                        "type": "bytes",
                        "logicalType": "decimal",
                        "precision": 3,
                        "scale": 2
                    },
                    "doc": "Discount number (from 0 to 1)"
                }
            ]
        }
    },
    {
        "oracle_table_name": "CATEGORY",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_category_fpd",
        "hive_format": "avro",
        "save_mode": "overwrite",
        "oracle_table_sql_query" : f"SELECT * FROM CATEGORY",
        "partition_field" : "None",
        "avro_schema_json" : {
            "type": "record",
            "name": "category",
            "namespace": "com.ods.avro",
            "fields": [
                {
                    "name": "category_id",
                    "type": "int",
                    "doc": "Unique identifier for table category"
                },
                {
                    "name": "category_name",
                    "type": "string",
                    "doc": "Name of category, like Clothing, Books, Grocery..."
                }
            ]
        }
    },
    {
        "oracle_table_name": "CUSTOMER",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_customer_fpd",
        "hive_format": "avro",
        "save_mode": "overwrite",
        "oracle_table_sql_query" : f"select * from CUSTOMER",
        "partition_field" : "None",
        "avro_schema_json" : {
            "type": "record",
            "name": "customer",
            "namespace": "com.ods.avro",
            "fields": [
                {
                    "name": "customer_id",
                    "type": "int",
                    "doc": "Unique id for each row in table customer"
                },
                {
                    "name": "first_name",
                    "type": "string",
                    "doc": "First name for the customer"
                },
                {
                    "name": "last_name",
                    "type": "string",
                    "doc": "Last name for the customer"
                },
                {
                    "name": "email",
                    "type": "string",
                    "doc": "The email address for the customer"
                },
                {
                    "name": "country",
                    "type": "string",
                    "doc": "The country that the customer is from"
                }
            ]
        }
    },
    {
        "oracle_table_name": "CUSTOMER_PRODUCT_RATINGS",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_customer_product_ratings_ipd",
        "hive_format": "avro",
        # "save_mode": "append",
        "save_mode": "overwrite",
        "oracle_table_sql_query" : f"select * from CUSTOMER_PRODUCT_RATINGS",
        "partition_field" : "data_date",
        "avro_schema_json" : {
            "type": "record",
            "name": "customer_product_ratings",
            "namespace": "com.ods.avro",
            "fields": [
                {
                    "name": "customerproductrating_id",
                    "type": "int",
                    "doc": "Unique id for each row in table customer_product_ratings"
                },
                {
                    "name": "customer_id",
                    "type": "int",
                    "doc": "The customer gave the review and ratings"
                },
                {
                    "name": "product_id",
                    "type": "int",
                    "doc": "The product that was given the review and ratings"
                },
                {
                    "name": "ratings",
                    "type": {
                        "type": "bytes",
                        "logicalType": "decimal",
                        "precision": 2,
                        "scale": 1
                    },
                    "doc": "The ratings specific number"
                },
                {
                    "name": "review",
                    "type": [
                        "null",
                        "string"
                    ],
                    "default": null,
                    "doc": "The review text"
                },
                {
                    "name": "sentiment",
                    "type": [
                        "null",
                        "string"
                    ],
                    "default": null,
                    "doc": "The final sentiment ('good' or 'bad')"
                }
            ]
        }
    },
    {
        "oracle_table_name": "MARKETING_CAMPAIGNS",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_marketing_campaigns_fpd",
        "hive_format": "avro",
        "save_mode": "overwrite",
        "oracle_table_sql_query" : f"select * from MARKETING_CAMPAIGNS",
        "partition_field" : "None",
        "avro_schema_json" : {
            "type": "record",
            "name": "marketing_campaigns",
            "namespace": "com.ods.avro",
            "fields": [
                {
                    "name": "campaign_id",
                    "type": "int",
                    "doc": "Unique id for each row in table marketing_campaigns"
                },
                {
                    "name": "campaign_name",
                    "type": "string",
                    "doc": "The campaign name"
                },
                {
                    "name": "offer_week",
                    "type": "int",
                    "doc": "Represents the ordinal of a year"
                }
            ]
        }
    },
    {
        "oracle_table_name": "ORDERS",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_orders_ipd",
        "hive_format": "avro",
        # "save_mode": "append",
        "save_mode": "overwrite",
        "oracle_table_sql_query" : f"select * from ORDERS",
        "partition_field" : "data_date",
        "avro_schema_json" : {
            "type": "record",
            "name": "orders",
            "namespace": "com.ods.avro",
            "fields": [
                {
                    "name": "order_id_surrogate",
                    "type": "int",
                    "doc": "Unique id for each row in table orders"
                },
                {
                    "name": "order_id",
                    "type": "int",
                    "doc": "Id for orders, could be duplicated"
                },
                {
                    "name": "customer_id",
                    "type": "int",
                    "doc": "The customer associated with the order"
                },
                {
                    "name": "order_date",
                    "type": {
                        "type": "int",
                        "logicalType": "date"
                    },
                    "doc": "The date generated on the order"
                },
                {
                    "name": "campaign_id",
                    "type": ["null", "int"],
                    "default": null,
                    "doc": "The campaign associated with the order"
                },
                {
                    "name": "amount",
                    "type": "int",
                    "doc": "The amount in this order associated with the order"
                },
                {
                    "name": "payment_method_id",
                    "type": ["null", "int"],
                    "default": null,
                    "doc": "The Payment Method for this order"
                }
            ]
        }
    },
    {
        "oracle_table_name": "ORDERITEM",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_orderitem_ipd",
        "hive_format": "avro",
        # "save_mode": "append",
        "save_mode": "overwrite",
        "oracle_table_sql_query" : f"select * from ORDERITEM",
        "partition_field" : "data_date",
        "avro_schema_json" : {
            "type": "record",
            "name": "orderitem",
            "namespace": "com.ods.avro",
            "fields": [
                {
                    "name": "orderitem_id",
                    "type": "int",
                    "doc": "Unique id for each row in table orderitem"
                },
                {
                    "name": "order_id",
                    "type": "int",
                    "doc": "To find the order in table orders"
                },
                {
                    "name": "product_id",
                    "type": "int",
                    "doc": "To find the product in the table products"
                },
                {
                    "name": "quantity",
                    "type": "int",
                    "doc": "The quantity of each product under this order"
                },
                {
                    "name": "supplier_id",
                    "type": "int",
                    "doc": "To find the supplier in the table supplier"
                },
                {
                    "name": "subtotal",
                    "type": {
                        "type": "bytes",
                        "logicalType": "decimal",
                        "precision": 10,
                        "scale": 2
                    },
                    "doc": "The subtotal amount for this order (quantity times price)"
                },
                {
                    "name": "discount",
                    "type": {
                        "type": "bytes",
                        "logicalType": "decimal",
                        "precision": 5,
                        "scale": 2
                    },
                    "doc": "The discount for this order"
                }
            ]
        }
    },
    {
        "oracle_table_name": "PAYMENT_METHOD",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_payment_method_fpd",
        "hive_format": "avro",
        "save_mode": "overwrite",
        "oracle_table_sql_query" : f"select * from PAYMENT_METHOD",
        "partition_field" : "None",
        "avro_schema_json" : {
            "type": "record",
            "name": "payment_method",
            "namespace": "com.ods.avro",
            "fields": [
                {
                    "name": "payment_method_id",
                    "type": "int",
                    "doc": "Unique id for payment method"
                },
                {
                    "name": "payment_method",
                    "type": "string",
                    "doc": "Payment method name"
                }
            ]
        }
    },
    {
        "oracle_table_name": "PRODUCT",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_product_fpd",
        "hive_format": "avro",
        "save_mode": "overwrite",
        "oracle_table_sql_query" : f"select * from PRODUCT",
        "partition_field" : "None",
        "avro_schema_json" : {
            "type": "record",
            "name": "product",
            "namespace": "com.ods.avro",
            "fields": [
                {
                    "name": "product_id",
                    "type": "int",
                    "doc": "Unique id for each row in table product"
                },
                {
                    "name": "name",
                    "type": "string",
                    "doc": "Name for product"
                },
                {
                    "name": "price",
                    "type": {
                        "type": "bytes",
                        "logicalType": "decimal",
                        "precision": 10,
                        "scale": 2
                    },
                    "doc": "Price for product, decimal with 2 places"
                },
                {
                    "name": "description",
                    "type": "string",
                    "doc": "Product description"
                },
                {
                    "name": "subcategory_id",
                    "type": "int",
                    "doc": "Foreign key to subcategory"
                }
            ]
        }
    },
    {
        "oracle_table_name": "RETURNS",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_returns_ipd",
        "hive_format": "avro",
        # "save_mode": "append",
        "save_mode": "overwrite",
        "oracle_table_sql_query" : f"select * from RETURNS",
        "partition_field" : "data_date",
        "avro_schema_json" : {
            "type": "record",
            "name": "returns",
            "namespace": "com.ods.avro",
            "fields": [
                {"name": "return_id", "type": "int", "doc": "Unique id for each row in table returns"},
                {"name": "order_id", "type": "int", "doc": "The order associated with the returned order"},
                {"name": "product_id", "type": "int", "doc": "The product associated with the returned order"},
                {"name": "return_date", "type": {"type": "string", "logicalType": "date"}, "doc": "The returned date for this order"},
                {"name": "reason", "type": ["null", "string"], "default": null, "doc": "The reason why customer returned this order"},
                {"name": "amount_refunded", "type": {"type": "bytes", "logicalType": "decimal", "precision": 10, "scale": 2}, "doc": "The amount refunded to the customer"}
            ]
        }
    },
    {
        "oracle_table_name": "SUBCATEGORY",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_subcategory_fpd",
        "hive_format": "avro",
        "save_mode": "overwrite",
        "oracle_table_sql_query" : f"select * from SUBCATEGORY",
        "partition_field" : "None",
        "avro_schema_json" : {
            "type": "record",
            "name": "subcategory",
            "namespace": "com.ods.avro",
            "fields": [
                {
                    "name": "subcategory_id",
                    "type": "int",
                    "doc": "Unique id for subcategory"
                },
                {
                    "name": "subcategory_name",
                    "type": "string",
                    "doc": "Subcategory name"
                },
                {
                    "name": "category_id",
                    "type": "int",
                    "doc": "Link to table category"
                }
            ]
        }
    },
    {
        "oracle_table_name": "SUPPLIER",
        "hive_hdfs_table_path": "/user/hive/warehouse/ods/ods_supplier_fpd",
        "hive_format": "avro",
        "save_mode": "overwrite",
        "oracle_table_sql_query" : f"select * from SUPPLIER",
        "partition_field" : "None",
        "avro_schema_json" : {
            "type": "record",
            "name": "supplier",
            "namespace": "com.ods.avro",
            "fields": [
                {
                    "name": "supplier_id",
                    "type": "int",
                    "doc": "Unique id for supplier"
                },
                {
                    "name": "supplier_name",
                    "type": "string",
                    "doc": "Name for supplier"
                },
                {
                    "name": "email",
                    "type": "string",
                    "doc": "Email for supplier"
                }
            ]
        }
    }
]
