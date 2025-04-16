#!/bin/bash

PORT1=8080
PORT2=8793
MAX_WAIT=120
COUNT=0

set -e

source /opt/airflow/airflow-env/bin/activate  # enter the virtual environment

echo "airflow container: launch airflow services: webserver"
nohup /opt/airflow/airflow-env/bin/airflow webserver -p 8080 > /root/airflow/airflow-webserver.log 2>&1 &

# listening whether port 8080 is open or not
while true; do
  if nc -z localhost $PORT1; then
    echo "airflow container: port 8080 is open and listening"
    echo "airflow container: successful to launch airflow webserver, port is 8080"
    echo "airflow container: launch airflow services: scheduler"
    nohup /opt/airflow/airflow-env/bin/airflow scheduler > /root/airflow/airflow-scheduler.log 2>&1 &
    break
  fi
  sleep 1
  COUNT=$((COUNT+1))
  if [ $COUNT -ge $MAX_WAIT ]; then
    echo "airflow container: Timeout: port $PORT1 not open"
    echo "airflow container: FAILED to launch airflow webserver"
    exit 1
  fi
done

COUNT=0

# listening whether port 8793 is open or not
while true; do
  if nc -z localhost $PORT2; then
    echo "airflow container: port 8793 is open and listening"
    echo "airflow container: successful to launch airflow scheduler, port is 8793"
    echo "airflow container: Finished launching airflow services"
    break
  fi
  sleep 1
  COUNT=$((COUNT+1))
  if [ $COUNT -ge $MAX_WAIT ]; then
    echo "airflow container: Timeout: port $PORT2 not open"
    echo "airflow container: FAILED to launch airflow services"
    exit 1
  fi
done
