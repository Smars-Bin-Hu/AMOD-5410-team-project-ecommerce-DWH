#!/bin/bash

PORT=10000
MAX_WAIT=120
COUNT=0

set -e

echo "Spark container: launch spark services: ThriftServer"
/opt/spark/sbin/start-thriftserver.sh \
  --master yarn \
  --conf spark.sql.hive.metastore.version=3.1.3 \
  --conf spark.sql.hive.metastore.jars=path \
  --conf spark.hadoop.hive.metastore.uris=thrift://hive:9083 \
  --conf spark.sql.warehouse.dir=hdfs://ns-ha/user/hive/warehouse

# listening whether port 10000 is open or not
while true; do
  if nc -z localhost $PORT; then
    echo "spark container: port 10000 is open and listening"
    break
  fi
  sleep 1
  COUNT=$((COUNT+1))
  if [ $COUNT -ge $MAX_WAIT ]; then
    echo "spark container: Timeout: port $PORT not open"
    exit 1
  fi
done

echo "spark container: Finished launch Spark services"