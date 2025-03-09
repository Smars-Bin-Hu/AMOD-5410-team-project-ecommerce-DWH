CREATE EXTERNAL TABLE IF NOT EXISTS ods_customer_fpd (
    customer_id INT COMMENT 'Unique id for each row in table customer',
    first_name STRING COMMENT 'First name for the customer',
    last_name STRING COMMENT 'Last name for the customer',
    email STRING COMMENT 'The email address for the customer',
    country STRING COMMENT 'The country that the customer is from'
)
COMMENT 'ODS Table for Customer (Daily Full Sync, Permenant Storage)'
ROW FORMAT SERDE
    'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS 
    INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/user/hive/warehouse/ods/ods_customer_fpd'
TBLPROPERTIES (
    'avro.schema.url'='hdfs:///user/hive/warehouse/ods/schema/ods_customer_fpd.avsc',
    'serialization.null.format'=''
);
