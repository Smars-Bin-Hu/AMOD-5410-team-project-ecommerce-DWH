#!/bin/bash

PORT1=10000
PORT2=10002
MAX_WAIT=120
COUNT=0

set -e

echo "hive container: stop hive services: hiveserver2"
netstat -nltp | grep ':10000' | awk '{print $7}' | cut -d'/' -f1 | xargs -r kill -9

sleep 5

echo "hive container: stop hive services: metastore"
netstat -nltp | grep ':9083' | awk '{print $7}' | cut -d'/' -f1 | xargs -r kill -9

sleep 5

# listening whether port 10000 and 9083 are both down
while true; do
  if ! nc -z localhost $PORT1 && ! nc -z localhost $PORT2; then
    echo "hive container: port 9083 and port 10000 are both already down"
    echo "hive container: successfully finished to stop hive services"
    break
  fi
  sleep 1
  COUNT=$((COUNT+1))
  if [ $COUNT -ge $MAX_WAIT ]; then
    echo "hive container: Timeout"
    echo "hive container: FAILED to finish to stop hive services"
    exit 1
  fi
done
