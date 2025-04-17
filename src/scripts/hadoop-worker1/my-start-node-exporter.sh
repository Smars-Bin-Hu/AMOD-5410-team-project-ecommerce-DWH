#!/bin/bash

# source the environment variable PATH
export PATH=/usr/local/bin

echo "Launching prometheus node exporter(port 9100) on hadoop-worker1"
set -e
node_exporter &