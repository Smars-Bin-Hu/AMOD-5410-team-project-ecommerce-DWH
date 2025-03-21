DROP TABLE IF EXISTS dwd.dwd_campaign_product_subcategory_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwd.dwd_campaign_product_subcategory_fpd
(
    campaign_product_subcategory_id INT             COMMENT 'Unique id for each row in table campaign_product_subcategory',
    campaign_id                     INT             COMMENT 'Campaign id (16 in total)',
    subcategory_id                  INT             COMMENT 'Subcategory id (100 in total)',
    discount                        DECIMAL(3, 2)   COMMENT 'Discount number (from 0 to 1)'
)
    COMMENT 'DWD Table for Campaign Product Subcategory (Daily Full Sync, Permenant Storage)'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dwd/dwd_campaign_product_subcategory_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );

