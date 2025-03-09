CREATE EXTERNAL TABLE IF NOT EXISTS ods_product_fpd (
    product_id INT COMMENT 'Unique id for each row in table product',
    name STRING COMMENT 'Name for product',
    price DECIMAL(10,2) COMMENT 'Price for product, decimal with 2 places',
    description STRING COMMENT 'Product description',
    subcategory_id INT COMMENT 'Foreign key to subcategory'
)
COMMENT 'ODS Table for Product (Daily Full Sync, Permenant Storage)'
ROW FORMAT SERDE
    'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS 
    INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/user/hive/warehouse/ods/ods_product_fpd'
TBLPROPERTIES (
    'avro.schema.url'='hdfs:///user/hive/warehouse/ods/schema/ods_product_fpd.avsc',
    'serialization.null.format'=''
);