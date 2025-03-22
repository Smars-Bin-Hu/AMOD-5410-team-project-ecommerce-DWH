docker exec -it --user root spark bash

$SPARK_HOME/sbin/start-thriftserver.sh \
    --master yarn \
    --conf spark.sql.hive.metastore.version=3.1.3 \
    --conf spark.sql.hive.metastore.jars=path \
    --conf spark.hadoop.hive.metastore.uris=thrift://hive:9083 \
    --conf spark.sql.warehouse.dir=hdfs://ns-ha/user/hive/warehouse
