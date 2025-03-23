#!/bin/bash

#####################################################################
#                                                                   #
#     mysql-metadata-restore.sh                                     #
#     1. restore metadata in MySQL(hive metastore)                  #
#      (This is used for your first use the metastore container)    #
#      You could use this script again if you wanna restore         #
#      the metadata on the mysql container                          #
#      path: /var/opt/all_databases_backup.sql                      #
#                                                                   #
#####################################################################

set -e

echo "[1] restore metadata in MySQL(hive metastore)"
docker exec -i mysql-hive-metastore bash -c "restore-mysql.sh"