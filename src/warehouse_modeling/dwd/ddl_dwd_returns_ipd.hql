DROP TABLE IF EXISTS dwd.dwd_returns_ipd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwd.dwd_returns_ipd
(
    return_id       INT             COMMENT 'Unique id for each row in table returns',
    order_id        INT             COMMENT 'The order associated with the returned order',
    product_id      INT             COMMENT 'The product associated with the returned order',
    return_date     STRING          COMMENT 'The returned date for this order',
    reason          STRING          COMMENT 'The reason why customer returned this order',
    amount_refunded DECIMAL(10, 2)  COMMENT 'The amount refunded to the customer'
)
    COMMENT 'DWD Table for Returns (Daily Incremental Sync, Permenant Storage)'
    PARTITIONED BY (DATA_DATE STRING COMMENT 'Data load date')
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dwd/dwd_returns_ipd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );
