#!/bin/bash

PORT1=9083
PORT2=10000
MAX_WAIT=120
COUNT=0

set -e

echo "hive container: launch hive services: metastore"
nohup $HIVE_HOME/bin/hive --service metastore >/dev/null 2>&1 &

# listening whether port 9083 is open or not
while true; do
  if nc -z localhost $PORT1; then
    echo "hive container: port 9083 is open and listening"
    echo "hive container: successful to launch metastore"
    echo "hive container: launch hive services: hiveserver2"
    nohup $HIVE_HOME/bin/hive --service hiveserver2 >/dev/null 2>&1 &
    break
  fi
  sleep 1
  COUNT=$((COUNT+1))
  if [ $COUNT -ge $MAX_WAIT ]; then
    echo "hive container: Timeout: port $PORT1 not open"
    echo "hive container: FAILED to launch metastore"
    exit 1
  fi
done

COUNT=0

# listening whether port 10000 is open or not
while true; do
  if nc -z localhost $PORT2; then
    echo "hive container: port 10000 is open and listening"
    echo "hive container: successful to launch hiveserver2"
    echo "hive container: Finished launching hive services"
    break
  fi
  sleep 1
  COUNT=$((COUNT+1))
  if [ $COUNT -ge $MAX_WAIT ]; then
    echo "hive container: Timeout: port $PORT2 not open"
    echo "hive container: FAILED to launch hiveserver2"
    exit 1
  fi
done

