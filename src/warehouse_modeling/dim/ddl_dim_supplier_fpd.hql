DROP TABLE IF EXISTS dim.dim_supplier_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS dim.dim_supplier_fpd
(
    supplier_id         INT     COMMENT 'Supplier id',
    supplier_name       STRING  COMMENT 'Supplier name',
    supplier_email      STRING  COMMENT 'Supplier email'
)
    COMMENT 'DIM Table for supplier info - Daily Full Sync, Permenant Storage'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dim/dim_supplier_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );