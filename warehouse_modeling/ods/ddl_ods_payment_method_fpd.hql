CREATE EXTERNAL TABLE IF NOT EXISTS ods_payment_method_fpd (
    payment_method_id INT COMMENT 'Unique id for payment method',
    payment_method STRING COMMENT 'Payment method name'
)
COMMENT 'ODS Table for Payment Method (Daily Full Sync, Permenant Storage)'
ROW FORMAT SERDE
    'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS 
    INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/user/hive/warehouse/ods/ods_payment_method_fpd'
TBLPROPERTIES (
    'avro.schema.url'='hdfs:///user/hive/warehouse/ods/schema/ods_payment_method_fpd.avsc',
    'serialization.null.format'=''
);