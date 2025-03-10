DROP TABLE ods.ods_orderitem_ipd;
CREATE EXTERNAL TABLE IF NOT EXISTS ods.ods_orderitem_ipd (
    orderitem_id INT COMMENT 'Unique id for each row in table orderitem',
    order_id INT COMMENT 'To find the order in table orders', -- AVRO
    product_id INT COMMENT 'To find the product in the table products',
    quantity INT COMMENT 'The quantity of each product under this order',
    supplier_id INT COMMENT 'To find the supplier in the table supplier',
    subtotal DECIMAL(10,2) COMMENT 'The subtotal amount for this order (quantity times price)',
    discount DECIMAL(5,2) COMMENT 'The discount for this order'
)
COMMENT 'ODS Table for Order Items (Daily Incremental Sync, Permenant Storage)'
PARTITIONED BY (DATA_DATE STRING COMMENT 'Data load date')
ROW FORMAT SERDE
    'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS 
    INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/user/hive/warehouse/ods/ods_orderitem_ipd'
TBLPROPERTIES (
    'avro.schema.url'='hdfs:///user/hive/warehouse/ods/schema/ods_orderitem_ipd.avsc',
    'serialization.null.format'=''
);
