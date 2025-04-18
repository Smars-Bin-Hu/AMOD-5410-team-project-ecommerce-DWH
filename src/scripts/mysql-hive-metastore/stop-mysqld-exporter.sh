#!/bin/bash

# source the environment variable PATH
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

PORT=9104
MAX_WAIT=120
COUNT=0

echo "stop mysqld-exporter on mysql-hive-metastore container"
netstat -nltp | grep ':9104' | awk '{print $7}' | cut -d'/' -f1 | xargs -r kill -15

while true; do
  if ! nc -z localhost $PORT; then
      echo "mysql-hive-metastore container: port 9104 is already down"
      echo "mysql-hive-metastore container: successfully stop mysqld-exporter on mysql-hive-metastore container"
      break
    fi
    sleep 1
    COUNT=$((COUNT+1))
    if [ $COUNT -ge $MAX_WAIT ]; then
      echo "mysql-hive-metastore container: Timeout"
      echo "mysql-hive-metastore container: FAILED to stop mysqld-exporter on mysql-hive-metastore container"
      exit 1
    fi
done