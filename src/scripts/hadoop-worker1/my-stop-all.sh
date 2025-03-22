#!/bin/bash

# source the environment so that Zookeeper/Hadoop is on PATH
export PATH=/usr/local/opt/module/zookeeper/bin:/usr/local/opt/module/sqoop/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/opt/module/hadoop/bin:/usr/local/opt/module/hadoop/sbin:/usr/local/opt/module/hive/bin

set -e

echo "[Stoping JournalNode on hadoop-worker1]"
nohup hdfs --daemon stop journalnode >/dev/null 2>&1 &

echo "[Stoping ZooKeeper on hadoop-worker1]"
nohup zkServer.sh stop >/dev/null 2>&1 &

sleep 3
echo "[Shutdown complete on hadoop-worker1]"
