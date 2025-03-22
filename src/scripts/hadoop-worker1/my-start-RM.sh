#!/bin/bash

# source the environment so that Zookeeper/Hadoop is on PATH
export PATH=/usr/local/opt/module/zookeeper/bin:/usr/local/opt/module/sqoop/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/opt/module/hadoop/bin:/usr/local/opt/module/hadoop/sbin:/usr/local/opt/module/hive/bin

echo "Launching ResourceManager on hadoop-worker1"
set -e
nohup yarn --daemon start resourcemanager >/dev/null 2>&1 &