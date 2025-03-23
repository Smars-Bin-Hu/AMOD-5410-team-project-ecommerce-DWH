#!/bin/bash

#####################################################################
#                                                                   #
#     start-data-clients.sh                                         #
#     1. launch hive services: metastore && hiveserver2             #
#     2. launch Spark service: ThriftServer                         #
#                                                                   #
#     IMPORTANT!!!!!                                                #
#     Prerequisite:                                                 #
#     make sure you already restore the metastore by running        #
#     the script `mysql-metadata-restore.sh`, and the `metastore`   #
#     database is already in the MySQL                              #
#     PATH: /var/lib/mysql/metastore  is existing                   #
#                                                                   #
#####################################################################

set -e

echo "[1] launch hive services: metastore && hiveserver2"
docker exec -i hive bash -c "start-hive-services.sh"

sleep 3

echo "[2] launch spark services: ThriftServer"
docker exec -i spark bash -c "start-spark-services.sh"

echo "FINISHED: launch hive && spark services"