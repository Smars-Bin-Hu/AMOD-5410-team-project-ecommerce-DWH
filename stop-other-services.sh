#!/bin/bash

#####################################################################
#                                                                   #
#     stop-other-services.sh                                        #
#     1. stop airflow services: webserver && scheduler              #
#     2. stop monitoring service:                                   #
#                                                                   #
#                                                                   #
#####################################################################

set -e

echo "[1] stop airflow services: ThriftServer"
docker exec -i airflow bash -c  "stop-airflow.sh"

sleep 3

echo "[2] stop monitoring services: "

echo "FINISHED: stop other services: airflow, monitoring"