DROP TABLE IF EXISTS dwd.dwd_product_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwd.dwd_product_fpd
(
    product_id     INT              COMMENT 'Unique id for each row in table product',
    name           STRING           COMMENT 'Name for product',
    price          DECIMAL(10, 2)   COMMENT 'Price for product, decimal with 2 places',
    description    STRING           COMMENT 'Product description',
    subcategory_id INT              COMMENT 'Foreign key to subcategory'
)
    COMMENT 'DWD Table for Product (Daily Full Sync, Permenant Storage)'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dwd/dwd_product_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );
