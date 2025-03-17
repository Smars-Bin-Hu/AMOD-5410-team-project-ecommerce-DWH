DROP TABLE IF EXISTS dim.dim_product_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dim.dim_product_fpd
(
    product_id             INT              COMMENT 'Product unique id',
    product_name           STRING           COMMENT 'Product name',
    price                  DECIMAL(8,2)     COMMENT 'Product Price',
    description            STRING           COMMENT 'Product Description',
    subcategory_id         INT              COMMENT 'The subcategory id that the product belongs to',
    subcategory_name       STRING           COMMENT 'The subcategory that the product belongs to',
    category_id            INT              COMMENT 'The category id that the product belongs to',
    category_name          STRING           COMMENT 'The category that the product belongs to'
)
    COMMENT 'DIM Table for product info - Daily Full Sync, Permenant Storage'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dim/dim_product_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );