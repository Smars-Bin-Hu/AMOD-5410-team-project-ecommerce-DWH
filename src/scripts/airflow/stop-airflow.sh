#!/bin/bash

PORT1=8080
PORT2=8793
MAX_WAIT=120
COUNT=0

set -e

echo "airflow container: stop airflow services"
ps -ef|egrep "scheduler|airflow-webserver" |grep -v grep | awk '{print $2}' | xargs kill -15

sleep 5

# listening whether port 8080 and 8793 are both down
while true; do
  if ! nc -z localhost $PORT1 && ! nc -z localhost $PORT2; then
    echo "airflow container: port 8080 and port 8793 are both already down"
    echo "airflow container: successfully finished to stop airflow services"
    break
  fi
  sleep 1
  COUNT=$((COUNT+1))
  if [ $COUNT -ge $MAX_WAIT ]; then
    echo "airflow container: Timeout: port $PORT is still open"
    echo "airflow container: FAILED to finish to stop airflow services"
    exit 1
  fi
done
