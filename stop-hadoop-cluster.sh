#!/bin/bash

set -e

echo "[1] Stop Services on the all Hadoop Cluster nodes"
for node in hadoop-master hadoop-worker1 hadoop-worker2; do
  docker exec -i $node bash -c "my-stop-all.sh"
done