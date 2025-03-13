DROP TABLE IF EXISTS dwd.dwd_subcategory_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwd.dwd_subcategory_fpd
(
    subcategory_id   INT        COMMENT 'Unique id for subcategory',
    subcategory_name STRING     COMMENT 'Subcategory name',
    category_id      INT        COMMENT 'Link to table category'
)
    COMMENT 'DWD Table for Subcategory (Daily Full Sync, Permenant Storage) based on existing category'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dwd/dwd_subcategory_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );

