DROP TABLE ods.ods_orders_ipd;
CREATE EXTERNAL TABLE IF NOT EXISTS ods.ods_orders_ipd (
    order_id_surrogate INT COMMENT 'Unique id for each row in table orders',
    order_id INT COMMENT 'Id for orders, could be duplicated',
    customer_id INT COMMENT 'The customer associated with the order',
    order_date STRING COMMENT 'The date generated on the order', -- AVRO
    campaign_id INT COMMENT 'The campaign associated with the order',
    amount INT COMMENT 'The amount in this order associated with the order',
    payment_method_id INT COMMENT 'The Payment Method for this order'
)
COMMENT 'ODS Table for Orders (Daily Incremental Sync, Permenant Storage)'
PARTITIONED BY (DATA_DATE STRING COMMENT 'Data load date')
ROW FORMAT SERDE 
    'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS 
    INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/user/hive/warehouse/ods/ods_orders_ipd'
TBLPROPERTIES (
    'avro.schema.url'='hdfs:///user/hive/warehouse/ods/schema/ods_orders_ipd.avsc',
    'serialization.null.format'=''
);