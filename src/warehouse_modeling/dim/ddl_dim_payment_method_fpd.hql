DROP TABLE IF EXISTS dim.dim_payment_method_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dim.dim_payment_method_fpd
(
    payment_method_id   INT     COMMENT 'Payment method id',
    payment_method      STRING  COMMENT 'Payment method name'
)
    COMMENT 'DIM Table for payment method info - Daily Full Sync, Permenant Storage'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dws/dim_payment_method_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );