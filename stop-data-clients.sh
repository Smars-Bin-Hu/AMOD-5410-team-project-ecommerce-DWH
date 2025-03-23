#!/bin/bash

#####################################################################
#                                                                   #
#     stop-data-clients.sh                                          #
#     1. stop hive services: metastore && hiveserver2               #
#     2. stop Spark service: ThriftServer                           #
#                                                                   #
#####################################################################

set -e

echo "[1] stop spark services: ThriftServer"
docker exec -i spark bash -c "stop-spark-services.sh"

sleep 3

echo "[2] stop hive services: metastore && hiveserver2"
docker exec -i hive bash -c "stop-hive-services.sh"

echo "FINISHED: stop hive && spark services"