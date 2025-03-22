#!/bin/bash

# source the environment so that Zookeeper/Hadoop is on PATH
export PATH=/usr/local/opt/module/zookeeper/bin:/usr/local/opt/module/sqoop/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/opt/module/hadoop/bin:/usr/local/opt/module/hadoop/sbin:/usr/local/opt/module/hive/bin

set -e

echo "[Stoping ZKFC on hadoop-worker2]"
nohup hdfs --daemon stop zkfc >/dev/null 2>&1 &

echo "[Stoping JournalNode on hadoop-worker2]"
nohup hdfs --daemon stop journalnode >/dev/null 2>&1 &

echo "[Stoping ZooKeeper on hadoop-worker2]"
nohup zkServer.sh stop >/dev/null 2>&1 &

sleep 5
echo "[Shutdown complete on hadoop-worker2]"