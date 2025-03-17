#!/bin/bash

# HDFS Target Path
HDFS_BASE_PATH="/user/hive/warehouse/dws"

# DWM TABLES
TABLES=(
    "dws_orders_detailed_info_wide_ipd"
)

# Create External Table Directory
echo "Creating Hive external table locations on HDFS..."
for table in "${TABLES[@]}"; do
    hdfs dfs -mkdir -p "${HDFS_BASE_PATH}/${table}"
    hdfs dfs -chmod -R 777 ${HDFS_BASE_PATH}
    echo "Created: ${HDFS_BASE_PATH}/${table}"
done
echo "All external locations have been set up successfully!"
