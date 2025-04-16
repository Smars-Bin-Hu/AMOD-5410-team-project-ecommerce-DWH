#!/bin/bash

#####################################################################
#                                                                   #
#     start-other-services.sh                                       #
#     1. launch airflow services: webserver && scheduler            #
#     2. launch monitoring service:                                 #
#                                                                   #
#                                                                   #
#####################################################################

set -e

echo "[1] launch airflow services: webserver && scheduler"
docker exec -i airflow bash -c "start-airflow.sh"

sleep 3

echo "[2] launch monitoring services: "

echo "FINISHED: launch other services: airflow, monitoring"