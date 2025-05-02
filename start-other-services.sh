#!/bin/bash

#############################################################################
#                                                                           #
#     start-other-services.sh                                               #
#     1. launch airflow services: webserver && dags                         #
#     2. launch monitoring service:                                         #
#             node-exporter on the hadoop cluster                           #
#             mysqld exporter on the mysql container                        #
#             prometheus, grafana, alertmanager on monitoring container     #
#                                                                           #
#############################################################################

set -e

echo "[1] launch airflow services: webserver && scheduler"
docker exec -i airflow bash -c "start-airflow.sh"

sleep 3

echo "[2] launch monitoring services: "
echo "launch node exporter on the hadoop cluster"
docker exec -i hadoop-master bash -c "my-start-node-exporter.sh"
docker exec -i hadoop-worker1 bash -c "my-start-node-exporter.sh"
docker exec -i hadoop-worker2 bash -c "my-start-node-exporter.sh"

sleep 3

echo "launch mysqld exporter on the mysql container"
docker exec -i mysql-hive-metastore bash -c "start-mysqld-exporter.sh"

sleep 3

echo "launch prometheus, grafana, alertmanager on the monitoring container"
docker exec -i monitoring bash -c "start-monitoring-services.sh"

echo "FINISHED: launch other services: airflow, monitoring"