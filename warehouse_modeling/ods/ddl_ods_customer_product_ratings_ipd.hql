DROP TABLE ods.ods_customer_product_ratings_ipd;
CREATE EXTERNAL TABLE IF NOT EXISTS ods.ods_customer_product_ratings_ipd (
    customerproductrating_id INT COMMENT 'Unique id for each row in table customer_product_ratings',
    customer_id INT COMMENT 'The customer gave the review and ratings',
    product_id INT COMMENT 'The product that was given the review and ratings',
    ratings DECIMAL(2,1) COMMENT 'The ratings specific number',
    review STRING COMMENT 'The review text',
    sentiment STRING COMMENT 'The final sentiment ("good" or "bad")'
)
COMMENT 'ODS Table for Customer Product Ratings (Daily Incremental Sync, Permenant Storage)'
PARTITIONED BY (DATA_DATE STRING COMMENT 'Data load date')
ROW FORMAT SERDE 
    'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS 
    INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/user/hive/warehouse/ods/ods_customer_product_ratings_ipd'
TBLPROPERTIES (
    'avro.schema.url'='hdfs:///user/hive/warehouse/ods/schema/ods_customer_product_ratings_ipd.avsc',
    'serialization.null.format'=''
);
