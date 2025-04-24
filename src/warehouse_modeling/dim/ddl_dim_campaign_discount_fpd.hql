DROP TABLE IF EXISTS dim.dim_campaign_discount_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dim.dim_campaign_discount_fpd
(
    campaign_id         INT             COMMENT 'Campaign unique id',
    campaign_name       STRING          COMMENT 'Campaign name',
    subcategory_id      INT             COMMENT 'Product subcategory unique id',
    subcategory_name    STRING          COMMENT 'Product subcategory name',
    category_id         INT             COMMENT 'Product category unique id',
    category_name       STRING          COMMENT 'Product category name',
    offer_week          INT             COMMENT 'campaign offering week of the year',
    discount            DECIMAL(8,2)    COMMENT 'discount number for the campaign under this subcategory'
)
    COMMENT 'DIM Table for campaign information - Daily Full Sync, Permenant Storage'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dws/dim_campaign_discount_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );
