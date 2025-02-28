CREATE EXTERNAL TABLE IF NOT EXISTS ods_subcategory_fpd (
    subcategory_id INT COMMENT 'Unique id for subcategory',
    subcategory_name STRING COMMENT 'Subcategory name',
    category_id INT COMMENT 'Link to table category'
)
COMMENT 'ODS Table for Subcategory (Daily Incremental Sync, Permenant Storage)'
PARTITIONED BY (DATA_DATE STRING COMMENT 'Data load date')
ROW FORMAT SERDE 
    'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS 
    INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/user/hive/warehouse/ods/ods_subcategory_fpd'
TBLPROPERTIES (
    'avro.schema.url'='hdfs:///user/hive/warehouse/ods/schema/ods_subcategory_fpd.avsc',
    'serialization.null.format'=''
);
