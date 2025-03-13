DROP TABLE IF EXISTS dwd.dwd_customer_product_ratings_ipd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwd.dwd_customer_product_ratings_ipd
(
    customerproductrating_id INT COMMENT 'Unique id for each row in table customer_product_ratings',
    customer_id              INT COMMENT 'The customer gave the review and ratings',
    product_id               INT COMMENT 'The product that was given the review and ratings',
    ratings                  DECIMAL(2, 1) COMMENT 'The ratings specific number',
    review                   STRING COMMENT 'The review text',
    sentiment                STRING COMMENT 'The final sentiment ("good" or "bad")'
)
    COMMENT 'DWD Table for Customer Product Ratings (Daily Incremental Sync, Permenant Storage)'
    PARTITIONED BY (DATA_DATE STRING COMMENT 'Data load date')
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dwd/dwd_customer_product_ratings_ipd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );