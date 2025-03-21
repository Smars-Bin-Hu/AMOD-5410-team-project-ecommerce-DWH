# MySQL metastore commands

1. MySQL dump .sql file to mysql-metastore container
```sql
mysqldump -u root -p --all-databases > /var/opt/all_databases_backup.sql
```

2. MySQL Partition Tables refresh
```bash
MSCK REPAIR TABLE <schema_name>.<table_name>
```

3. Check the `Hive` metadata in the `MySQL`
```sql
SELECT TBL_ID, DB_ID, TBL_NAME, TBL_TYPE FROM TBLS WHERE TBL_NAME = '<table_name>';
SELECT SD_ID, LOCATION FROM SDS WHERE SD_ID = (SELECT SD_ID FROM TBLS WHERE TBL_NAME = '<table_name>');
SELECT PARAM_KEY, PARAM_VALUE FROM TABLE_PARAMS WHERE TBL_ID = (SELECT TBL_ID FROM TBLS WHERE TBL_NAME = '<table_name>');
SELECT PKEY_NAME, PKEY_TYPE FROM PARTITION_KEYS WHERE TBL_ID = (SELECT TBL_ID FROM TBLS WHERE TBL_NAME = '<table_name>');
```

for partition tables only
```sql
SELECT * FROM PARTITIONS;
SELECT PART_ID, PART_NAME, TBL_ID FROM PARTITIONS WHERE TBL_ID = (SELECT TBL_ID FROM TBLS WHERE TBL_NAME = '<table_name>');
```

4. add partitions metadata manually
```sql
INSERT INTO PARTITIONS (PART_ID, PART_NAME, TBL_ID, SD_ID, CREATE_TIME, LAST_ACCESS_TIME)
SELECT
COALESCE(MAX_PART_ID + 1, 1) AS PART_ID,
'data_date=2024-03-10', -- change the partition field
tbl.TBL_ID,
sd.SD_ID + 1,
UNIX_TIMESTAMP(),
0
FROM
(SELECT COALESCE(MAX(PART_ID), 0) AS MAX_PART_ID FROM PARTITIONS) AS p,
(SELECT TBL_ID FROM TBLS WHERE TBL_NAME = '<table_name>') AS tbl,
(SELECT SD_ID FROM SDS ORDER BY SD_ID DESC LIMIT 1) AS sd;
```

5. Lock and Kill
```sql
SHOW FULL PROCESSLIST;
```

```sql
KILL
```
