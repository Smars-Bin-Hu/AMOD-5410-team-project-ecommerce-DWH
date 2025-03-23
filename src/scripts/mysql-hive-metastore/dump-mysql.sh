#!/bin/bash

# source the environment so that mysql is on PATH
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

echo "Dump mysql all databases on mysql-hive-metastore container"
set -e

# This mysql database is the metastore for hive,
# the password is public for your local testing
nohup mysqldump -u root -pWhos3301919! --all-databases > /var/opt/all_databases_backup.sql >/dev/null 2>&1 &
echo "FINISHED: Dump mysql all databases on mysql-hive-metastore container"