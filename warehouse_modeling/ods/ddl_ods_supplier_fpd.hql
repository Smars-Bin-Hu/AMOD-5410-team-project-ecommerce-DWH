CREATE EXTERNAL TABLE IF NOT EXISTS ods_supplier_fpd (
    supplier_id INT COMMENT 'Unique id for supplier',
    supplier_name STRING COMMENT 'Name for supplier',
    email STRING COMMENT 'Email for supplier'
)
COMMENT 'ODS Table for Supplier (Daily Full Sync, Permenant Storage)'
PARTITIONED BY (DATA_DATE STRING COMMENT 'Data load date')
ROW FORMAT SERDE 
    'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS 
    INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/user/hive/warehouse/ods/ods_supplier_fpd'
TBLPROPERTIES (
    'avro.schema.url'='hdfs:///user/hive/warehouse/ods/schema/ods_supplier_fpd.avsc',
    'serialization.null.format'=''
);