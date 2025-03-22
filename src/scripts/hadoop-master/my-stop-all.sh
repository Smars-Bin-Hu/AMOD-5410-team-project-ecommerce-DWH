#!/bin/bash

# source the environment so that Zookeeper/Hadoop is on PATH
export PATH=/usr/local/opt/module/zookeeper/bin:/usr/local/opt/module/sqoop/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/opt/module/hadoop/bin:/usr/local/opt/module/hadoop/sbin:/usr/local/opt/module/hive/bin

set -e

echo "[Stoping HistoryServer]"
mr-jobhistory-daemon.sh stop historyserver

echo "[Stoping YARN on all 3 nodes]"
nohup stop-yarn.sh  >/dev/null 2>&1 &

echo "[Stoping HDFS on all 3 nodes]"
nohup stop-dfs.sh  >/dev/null 2>&1 &

sleep 15

echo "[Stoping JournalNode on hadoop-master]"
nohup hdfs --daemon stop journalnode >/dev/null 2>&1 &

echo "[Stoping ZooKeeper on hadoop-master]"
nohup zkServer.sh stop >/dev/null 2>&1 &

sleep 5
echo "[Shutdown complete on hadoop-master]"
