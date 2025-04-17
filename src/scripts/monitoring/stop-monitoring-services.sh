#!/bin/bash

PORT1=9090
PORT2=9093
PORT3=9094
PORT4=3000
MAX_WAIT=120
COUNT=0

set -e

echo "monitoring container: stop services: grafana"
netstat -nltp | grep ':3000' | awk '{print $7}' | cut -d'/' -f1 | xargs -r kill -15

echo "monitoring container: stop services: alertmanager"
netstat -nltp | grep ':9093' | awk '{print $7}' | cut -d'/' -f1 | xargs -r kill -15

echo "monitoring container: stop services: alertmanager"
netstat -nltp | grep ':9094' | awk '{print $7}' | cut -d'/' -f1 | xargs -r kill -15

echo "monitoring container: stop services: prometheus"
netstat -nltp | grep ':9090' | awk '{print $7}' | cut -d'/' -f1 | xargs -r kill -15

while true; do
  if ! nc -z localhost $PORT1 && ! nc -z localhost $PORT2 && ! nc -z localhost $PORT3 && ! nc -z localhost $PORT4; then
      echo "monitoring container: port 9090, 3000, 9093, and 9094 are all already down"
      echo "monitoring container: successfully finished to stop monitoring services"
      break
    fi
    sleep 1
    COUNT=$((COUNT+1))
    if [ $COUNT -ge $MAX_WAIT ]; then
      echo "monitoring container: Timeout"
      echo "monitoring container: FAILED to finish to stop monitoring services"
      exit 1
    fi
done