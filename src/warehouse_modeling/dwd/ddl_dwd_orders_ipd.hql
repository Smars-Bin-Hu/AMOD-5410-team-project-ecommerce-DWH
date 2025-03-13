DROP TABLE IF EXISTS dwd.dwd_orders_ipd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwd.dwd_orders_ipd
(
    order_id_surrogate INT      COMMENT 'Unique id for each row in table orders',
    order_id           INT      COMMENT 'Id for orders, could be duplicated',
    customer_id        INT      COMMENT 'The customer associated with the order',
    order_date         STRING   COMMENT 'The date generated on the order',
    campaign_id        INT      COMMENT 'The campaign associated with the order',
    amount             INT      COMMENT 'The amount in this order associated with the order',
    payment_method_id  INT      COMMENT 'The Payment Method for this order'
)
    COMMENT 'DWD Table for Orders (Daily Incremental Sync, Permenant Storage)'
    PARTITIONED BY (DATA_DATE STRING COMMENT 'Data load date')
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dwd/dwd_orders_ipd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );