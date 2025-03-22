#!/bin/bash

# source the environment so that Zookeeper/Hadoop is on PATH
export PATH=/usr/local/opt/module/zookeeper/bin:/usr/local/opt/module/sqoop/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/opt/module/hadoop/bin:/usr/local/opt/module/hadoop/sbin:/usr/local/opt/module/hive/bin

echo "Launching Namenode + ZKFC on hadoop-worker2"
set -e
nohup hdfs --daemon start namenode >/dev/null 2>&1 &
nohup hdfs --daemon start zkfc >/dev/null 2>&1 &
