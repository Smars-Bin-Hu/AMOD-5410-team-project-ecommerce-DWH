#!/bin/bash

# HDFS Target Path
HDFS_BASE_PATH="/user/hive/warehouse/dwd"

# DWD TABLES
TABLES=(
    "dwd_campaign_product_subcategory_fpd"
    "dwd_category_fpd"
    "dwd_customer_fpd"
    "dwd_customer_product_ratings_ipd"
    "dwd_marketing_campaigns_fpd"
    "dwd_orders_ipd"
    "dwd_orderitem_ipd"
    "dwd_payment_method_fpd"
    "dwd_product_fpd"
    "dwd_returns_ipd"
    "dwd_subcategory_fpd"
    "dwd_supplier_fpd"
)

# Create External Table Directory
echo "Creating Hive external table locations on HDFS..."
for table in "${TABLES[@]}"; do
    hdfs dfs -mkdir -p "${HDFS_BASE_PATH}/${table}"
    hdfs dfs -chmod -R 777 ${HDFS_BASE_PATH}
    echo "Created: ${HDFS_BASE_PATH}/${table}"
done
echo "All external locations have been set up successfully!"
