DROP TABLE IF EXISTS dim.dim_customer_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dim.dim_customer_fpd
(
    customer_id INT     COMMENT 'Customer unique id',
    first_name  STRING  COMMENT 'Customer first name',
    last_name   STRING     COMMENT 'Customer last name',
    email       STRING  COMMENT 'Customer Email',
    country     STRING  COMMENT 'The country that the customer from'
)
    COMMENT 'DIM Table for customer info - Daily Full Sync, Permenant Storage'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dim/dim_customer_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );