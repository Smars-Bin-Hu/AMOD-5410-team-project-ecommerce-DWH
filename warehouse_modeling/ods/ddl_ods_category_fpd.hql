CREATE EXTERNAL TABLE IF NOT EXISTS ods_category_fpd (
    category_id INT COMMENT 'Unique identifier for table category',
    category_name STRING COMMENT 'Name of category, like Clothing, Books, Grocery...'
)
COMMENT 'ODS Table for Category (Daily Full Sync, Permenant Storage)'
PARTITIONED BY (DATA_DATE STRING COMMENT 'Data load date')
ROW FORMAT SERDE 
    'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS 
    INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/user/hive/warehouse/ods/ods_category_fpd'
TBLPROPERTIES (
    'avro.schema.url'='hdfs:///user/hive/warehouse/ods/schema/ods_category_fpd.avsc',
    'serialization.null.format'=''
);
