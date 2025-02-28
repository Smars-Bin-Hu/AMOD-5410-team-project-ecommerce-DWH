

##  Hive QL DDL Specification

This is what the HiveQL DDL should be.
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

- EXTERNAL：
  - external: the tables are stored on the HDFS, which need to be keep for a long time. 
  - internal: the tables that hive controls and manages totally, such as temporary analysis tasks or data sets that do not need to be stored for a long time.
- PARTITIONED BY：table partition
- CLUSTERED BY：table bucket
- ROW FORMAT：speficic the split character
  - row：\001
  - column：\n
- STORED AS：file storage format
- LOCATION：refer to HDFS files address
  - default: /user/hive/warehouse/dbdir/tbdir
- TBLPROPERTIES：specific other configuration for tables