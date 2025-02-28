CREATE EXTERNAL TABLE IF NOT EXISTS ods_campaign_product_subcategory_fpd (
    campaign_product_subcategory_id INT COMMENT 'Unique id for each row in table campaign_product_subcategory',
    campaign_id INT COMMENT 'Campaign id (16 in total)',
    subcategory_id INT COMMENT 'Subcategory id (100 in total)',
    discount DECIMAL(3,2) COMMENT 'Discount number (from 0 to 1)'
)
COMMENT 'ODS Table for Campaign Product Subcategory (Daily Full Sync, Permenant Storage)'
PARTITIONED BY (DATA_DATE STRING COMMENT 'Data load date')
ROW FORMAT SERDE 
    'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS 
    INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/user/hive/warehouse/ods/ods_campaign_product_subcategory_fpd'
TBLPROPERTIES (
    'avro.schema.url'='hdfs:///user/hive/warehouse/ods/schema/ods_campaign_product_subcategory_fpd.avsc',
    'serialization.null.format'=''
);
