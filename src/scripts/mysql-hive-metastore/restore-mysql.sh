#!/bin/bash

# source the environment so that mysql is on PATH
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

echo "restore mysql on mysql-hive-metastore container"
set -e

# This mysql database is the metastore for hive,
# the password is public for your local testing
nohup  mysql -u root -pWhos3301919! < /var/opt/all_databases_backup.sql >/dev/null 2>&1 &
echo "FINISHED: restore mysql on mysql-hive-metastore container"