#!/bin/bash

#############################################################################
#                                                                           #
#     stop-other-services.sh                                                #
#     1. stop airflow services: webserver && scheduler                      #
#     2. stop monitoring service:                                           #
#             node-exporter on the hadoop cluster                           #
#             mysqld exporter on the mysql container                        #
#             prometheus, grafana, alertmanager on monitoring container     #
#                                                                           #
#############################################################################

set -e

echo "[1] stop airflow services: webserver && scheduler"
docker exec -i airflow bash -c  "stop-airflow.sh"

sleep 3

echo "[2] stop monitoring services: "
echo "stop prometheus, grafana, alertmanager on the monitoring container"
docker exec -i monitoring bash -c "stop-monitoring-services.sh"

sleep 3

echo "stop node exporter on the hadoop cluster"
docker exec -i hadoop-master bash -c "my-stop-node-exporter.sh"
docker exec -i hadoop-worker1 bash -c "my-stop-node-exporter.sh"
docker exec -i hadoop-worker2 bash -c "my-stop-node-exporter.sh"

sleep 3

echo "stop mysqld exporter on the mysql container"
docker exec -i mysql-hive-metastore bash -c "stop-mysqld-exporter.sh"

echo "FINISHED: stop other services: airflow, monitoring"