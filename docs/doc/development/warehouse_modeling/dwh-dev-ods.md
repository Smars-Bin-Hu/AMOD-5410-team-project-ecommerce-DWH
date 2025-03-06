# Data Warehouse Development ODS Layer

### 1. Create ODS directory on the HDFS

HDFS is where the data stored, so we should create the directory in terms of base name(layer) and table name.

```bash
hdfs dfs -mkdir -p /user/hive/warehouse/ods/ods_campaign_product_subcategory_fpd
hdfs dfs -mkdir -p /user/hive/warehouse/ods/ods_category_fpd
hdfs dfs -mkdir -p /user/hive/warehouse/ods/ods_customer_fpd
hdfs dfs -mkdir -p /user/hive/warehouse/ods/ods_customer_product_ratings_ipd
hdfs dfs -mkdir -p /user/hive/warehouse/ods/ods_marketing_campaigns_fpd
hdfs dfs -mkdir -p /user/hive/warehouse/ods/ods_orderitem_ipd
hdfs dfs -mkdir -p /user/hive/warehouse/ods/ods_orders_ipd
hdfs dfs -mkdir -p /user/hive/warehouse/ods/ods_payment_method_fpd
hdfs dfs -mkdir -p /user/hive/warehouse/ods/ods_product_fpd
hdfs dfs -mkdir -p /user/hive/warehouse/ods/ods_returns_ipd
hdfs dfs -mkdir -p /user/hive/warehouse/ods/ods_subcategory_fpd
hdfs dfs -mkdir -p /user/hive/warehouse/ods/ods_supplier_fpd
```

Verify the creation

```bash
hdfs dfs -ls /dwh/ods
```

### 2. Hive QL

Hive should create the table schema to map the HDFS data files.

```sql

CREATE [TEMPORARY] [EXTERNAL] TABLE [IF NOT EXISTS] [db_name.]table_name
(
col1Name col1Type [COMMENT col_comment],
co21Name col2Type [COMMENT col_comment],
co31Name col3Type [COMMENT col_comment],
co41Name col4Type [COMMENT col_comment],
co51Name col5Type [COMMENT col_comment],
……
coN1Name colNType [COMMENT col_comment]
)
[PARTITIONED BY (col_name data_type ...)]
[CLUSTERED BY (col_name...) [SORTED BY (col_name ...)] INTO N BUCKETS]
[ROW FORMAT row_format]
row format delimited fields terminated by
lines terminated by
[STORED AS file_format]
[LOCATION hdfs_path]
TBLPROPERTIES
```
