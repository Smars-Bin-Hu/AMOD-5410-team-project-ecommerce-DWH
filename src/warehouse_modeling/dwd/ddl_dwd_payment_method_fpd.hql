DROP TABLE IF EXISTS dwd.dwd_payment_method_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwd.dwd_payment_method_fpd
(
    payment_method_id INT       COMMENT 'Unique id for payment method',
    payment_method    STRING    COMMENT 'Payment method name'
)
    COMMENT 'ODS Table for Payment Method (Daily Full Sync, Permenant Storage)'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dwd/dwd_payment_method_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );