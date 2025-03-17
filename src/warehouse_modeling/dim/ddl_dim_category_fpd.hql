DROP TABLE IF EXISTS dim.dim_category_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dim.dim_category_fpd
(
    category_id         INT     COMMENT 'Product category unique id',
    category_name       STRING  COMMENT 'Product category name',
    subcategory_id      INT     COMMENT 'Product subcategory unique id',
    subcategory_name    STRING  COMMENT 'Product subcategory name'
)
    COMMENT 'DIM Table for product category and subcategory info - Daily Full Sync, Permenant Storage'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dim/dim_category_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );
