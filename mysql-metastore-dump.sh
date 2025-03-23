#!/bin/bash

#####################################################################
#                                                                   #
#     mysql-metastore-dump.sh                                       #
#     -- dump all databases in MySQL(hive metastore)                #
#      You MUST use this script                                     #
#      for your first use the metastore container                   #
#                                                                   #
#      You could use this script again if you wanna restore         #
#      the metadata on the mysql container                          #
#                                                                   #
#      path on container: /var/opt/all_databases_backup.sql         #
#      MOUNTED BY DOCKER                                            #
#      ./src/infra/mysql-metastore-dump/all_databases_backup.sql    #
#                                                                   #
#####################################################################

set -e

echo "dump all databases in MySQL(hive metastore)"
docker exec -i mysql-hive-metastore bash -c "dump-mysql.sh"