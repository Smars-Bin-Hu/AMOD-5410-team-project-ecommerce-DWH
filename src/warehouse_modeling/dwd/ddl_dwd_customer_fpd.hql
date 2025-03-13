DROP TABLE IF EXISTS dwd.dwd_customer_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwd.dwd_customer_fpd
(
    customer_id INT     COMMENT 'Unique id for each row in table customer',
    first_name  STRING  COMMENT 'First name for the customer',
    last_name   STRING  COMMENT 'Last name for the customer',
    email       STRING  COMMENT 'The email address for the customer',
    country     STRING  COMMENT 'The country that the customer is from'
)
    COMMENT 'DWD Table for Customer (Daily Full Sync, Permenant Storage)'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dwd/dwd_customer_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );
