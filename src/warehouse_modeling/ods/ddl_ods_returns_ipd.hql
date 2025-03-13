DROP TABLE ods.ods_returns_ipd;
CREATE EXTERNAL TABLE IF NOT EXISTS ods.ods_returns_ipd (
    return_id INT COMMENT 'Unique id for each row in table returns',
    order_id INT COMMENT 'The order associated with the returned order',
    product_id INT COMMENT 'The product associated with the returned order',
    return_date STRING COMMENT 'The returned date for this order',
    reason STRING COMMENT 'The reason why customer returned this order',
    amount_refunded DECIMAL(10,2) COMMENT 'The amount refunded to the customer'
)
COMMENT 'ODS Table for Returns (Daily Incremental Sync, Permenant Storage)'
PARTITIONED BY (DATA_DATE STRING COMMENT 'Data load date')
ROW FORMAT SERDE 
    'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS 
    INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/user/hive/warehouse/ods/ods_returns_ipd'
TBLPROPERTIES (
    'avro.schema.url'='hdfs:///user/hive/warehouse/ods/schema/ods_returns_ipd.avsc',
    'serialization.null.format'=''
);