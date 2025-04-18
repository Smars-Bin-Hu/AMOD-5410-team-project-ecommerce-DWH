#!/bin/bash

#####################################################################
#                                                                   #
#     mysql-metadata-restore.sh                                     #
#     -- restore metadata in MySQL(hive metastore)                  #
#      You MUST use this script                                     #
#      for your first use the metastore container                   #
#                                                                   #
#      You could use this script again if you wanna restore         #
#      the metadata on the mysql container                          #
#                                                                   #
#      path on container: /var/opt/all_databases_backup.sql         #
#      MOUNTED BY DOCKER                                            #
#      ./src/infra/mysql-metastore-dunmp/all_databases_backup.sql    #
#                                                                   #
#####################################################################

set -e

echo "restore metadata in MySQL(hive metastore)"
docker exec -i mysql-hive-metastore bash -c "restore-mysql.sh"