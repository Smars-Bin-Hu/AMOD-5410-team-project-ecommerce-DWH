#!/bin/bash

# HDFS Target Path
HDFS_BASE_PATH="/user/hive/warehouse/dim"

# DWD TABLES
TABLES=(
    "dim_category_fpd"
    "dim_campaign_discount_fpd"
    "dim_customer_fpd"
    "dim_payment_method_fpd"
    "dim_product_fpd"
    "dim_supplier_fpd"
)

# Create External Table Directory
echo "Creating Hive external table locations on HDFS..."
for table in "${TABLES[@]}"; do
    hdfs dfs -mkdir -p "${HDFS_BASE_PATH}/${table}"
    hdfs dfs -chmod -R 777 ${HDFS_BASE_PATH}
    echo "Created: ${HDFS_BASE_PATH}/${table}"
done
echo "All external locations have been set up successfully!"
