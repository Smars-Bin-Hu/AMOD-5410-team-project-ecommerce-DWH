# Hive Metatdata Query and Refresh

## On the `MySQL` (metastore) Check the hive table metadata

Check the tables metadata
```mysql
SELECT TBL_ID, DB_ID, TBL_NAME, TBL_TYPE
FROM TBLS
WHERE TBL_NAME = 'ods_customer_product_ratings_ipd';
```
Check the HDFS location metadata
```mysql
SELECT SD_ID, LOCATION
FROM SDS
WHERE SD_ID = (SELECT SD_ID FROM TBLS WHERE TBL_NAME = 'ods_customer_product_ratings_ipd');
```
Check the table parameters
```mysql
SELECT PARAM_KEY, PARAM_VALUE
FROM TABLE_PARAMS
WHERE TBL_ID = (SELECT TBL_ID FROM TBLS WHERE TBL_NAME = 'ods_customer_product_ratings_ipd');
```

Check the Partitions (Partitioned Tables only)
```mysql
SELECT PART_ID, PART_NAME, TBL_ID FROM PARTITIONS
WHERE TBL_ID = (SELECT TBL_ID FROM TBLS WHERE TBL_NAME = 'ods_customer_product_ratings_ipd');
```

## On the `Hive` refresh the metadata

> after load data to HDFS, hive cannot know. so we should refresh the metadata and tell hive to scan the tables again. 

on `Hive` to show create ddl 
```hiveql
SHOW CREATE TABLE ods.ods_customer_product_ratings_ipd;
```

partition tables metadata refresh
```hiveql
MSCK REPAIR TABLE ods.ods_customer_product_ratings_ipd;
```

Let Hive scan HDFS again
```hiveql
ALTER TABLE ods.ods_customer_product_ratings_ipd SET TBLPROPERTIES ('EXTERNAL'='TRUE');
```

Manually Refresh (last and final choice)
```hiveql
DROP TABLE ods_customer_product_ratings_ipd;
CREATE EXTERNAL TABLE IF NOT EXISTS ods_customer_product_ratings_ipd (
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
```