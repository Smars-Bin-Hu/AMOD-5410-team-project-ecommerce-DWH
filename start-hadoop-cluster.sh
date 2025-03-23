#!/bin/bash

set -e

echo "[1] Launching Zookeeper + JournalNode on all nodes"
for node in hadoop-master hadoop-worker1 hadoop-worker2; do
  docker exec -i $node bash -c "my-start-zk.sh"
done

sleep 8

echo "[2] Launching Namenodes and ZKFC on hadoop-master and hadoop-worker2"
for node in hadoop-master hadoop-worker2; do
  docker exec -i $node bash -c "my-start-NN-ZKFC.sh"
done

sleep 5

echo "[3] Launching ResourceManager on hadoop-master and hadoop-worker1"
for node in hadoop-master hadoop-worker1; do
  docker exec -i $node bash -c "my-start-RM.sh"
done

sleep 5

echo "[4] Launching DataNode, NodeManager on all three nodes"
for node in hadoop-master hadoop-worker1 hadoop-worker2; do
  docker exec -i $node bash -c "my-start-NM-DN.sh"
done

sleep 3

echo "[5] Launching Job History Server on hadoop-master"
docker exec -i hadoop-master bash -c "my-start-historyserver.sh"

sleep 3
echo "[6] Turn off the safe mode for Namenodes"
docker exec -i hadoop-master bash -c "/usr/local/opt/module/hadoop/bin/hdfs dfsadmin -safemode leave"