DROP TABLE IF EXISTS dwd.dwd_supplier_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwd.dwd_supplier_fpd
(
    supplier_id   INT       COMMENT 'Unique id for supplier',
    supplier_name STRING    COMMENT 'Name for supplier',
    email         STRING    COMMENT 'Email for supplier'
)
    COMMENT 'DWD Table for Supplier (Daily Full Sync, Permenant Storage)'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dwd/dwd_supplier_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );
