DROP TABLE IF EXISTS dwd.dwd_category_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwd.dwd_category_fpd
(
    category_id   INT       COMMENT 'Unique identifier for table category',
    category_name STRING    COMMENT 'Name of category, like Clothing, Books, Grocery...'
)
    COMMENT 'DWD Table for Category (Daily Full Sync, Permenant Storage)'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dwd/dwd_category_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );

