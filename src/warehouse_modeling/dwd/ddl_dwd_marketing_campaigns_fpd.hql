DROP TABLE IF EXISTS dwd.dwd_marketing_campaigns_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwd.dwd_marketing_campaigns_fpd
(
    campaign_id   INT       COMMENT 'Unique id for each row in table marketing_campaigns',
    campaign_name STRING    COMMENT 'The campaign name',
    offer_week    INT       COMMENT 'Represents the ordinal of a year'
)
    COMMENT 'DWD Table for Marketing Campaigns (Daily Full Sync, Permenant Storage)'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dwd/dwd_marketing_campaigns_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );