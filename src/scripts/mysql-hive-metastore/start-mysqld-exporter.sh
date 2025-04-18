#!/bin/bash

# source the environment variable PATH
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export PATH=$PATH:/opt/mysqld_exporter

echo "Launching prometheus mysqld exporter(port 9104) on mysql-hive-metastore container"
set -e
mysqld_exporter \
  --config.my-cnf="/opt/mysqld_exporter/my.cnf" \
  --web.listen-address=":9104" &