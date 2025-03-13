DROP TABLE IF EXISTS dwd.dwd_orderitem_ipd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwd.dwd_orderitem_ipd
(
    orderitem_id INT            COMMENT 'Unique id for each row in table orderitem',
    order_id     INT            COMMENT 'To find the order in table orders',
    product_id   INT            COMMENT 'To find the product in the table products',
    quantity     INT            COMMENT 'The quantity of each product under this order',
    supplier_id  INT            COMMENT 'To find the supplier in the table supplier',
    subtotal     DECIMAL(10, 2) COMMENT 'The subtotal amount for this order (quantity times price)',
    discount     DECIMAL(5, 2)  COMMENT 'The discount for this order'
)
    COMMENT 'DWD Table for Order Items (Daily Incremental Sync, Permenant Storage)'
    PARTITIONED BY (DATA_DATE STRING COMMENT 'Data load date')
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dwd/dwd_orderitem_ipd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );