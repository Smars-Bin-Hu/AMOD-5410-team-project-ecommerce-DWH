DROP TABLE ods.ods_marketing_campaigns_fpd;
CREATE EXTERNAL TABLE IF NOT EXISTS ods.ods_marketing_campaigns_fpd (
    campaign_id INT COMMENT 'Unique id for each row in table marketing_campaigns',
    campaign_name STRING COMMENT 'The campaign name',
    offer_week INT COMMENT 'Represents the ordinal of a year'
)
COMMENT 'ODS Table for Marketing Campaigns (Daily Full Sync, Permenant Storage)'
ROW FORMAT SERDE
    'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS 
    INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/user/hive/warehouse/ods/ods_marketing_campaigns_fpd'
TBLPROPERTIES (
    'avro.schema.url'='hdfs:///user/hive/warehouse/ods/schema/ods_marketing_campaigns_fpd.avsc',
    'serialization.null.format'=''
);