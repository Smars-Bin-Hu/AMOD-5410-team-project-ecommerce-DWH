#!/bin/bash

#####################################################################
#                                                                   #
#     stop-other-services.sh                                        #
#     1. stop airflow services: webserver && scheduler              #
#     2. stop monitoring service:                                   #
#                                                                   #
#####################################################################

set -e

echo "[1] stop airflow services: webserver && scheduler"
docker exec -i airflow bash -c  "stop-airflow.sh"

sleep 3

echo "[2] stop monitoring services: "
echo "stop prometheus, grafana, alertmanager on the monitoring container"
docker exec -i monitoring bash -c "stop-monitoring-services.sh"

sleep 3

echo "stop node exporter on the hadoop master and workers"
docker exec -i hadoop-master bash -c "my-stop-node-exporter.sh"
docker exec -i hadoop-worker1 bash -c "my-stop-node-exporter.sh"
docker exec -i hadoop-worker2 bash -c "my-stop-node-exporter.sh"

echo "FINISHED: stop other services: airflow, monitoring"