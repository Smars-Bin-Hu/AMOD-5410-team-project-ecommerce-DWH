#!/bin/bash

# HDFS Target Path
HDFS_BASE_PATH="/user/hive/warehouse/ods"
SCHEMA_HDFS_PATH="${HDFS_BASE_PATH}/schema"

# ODS TABLES
TABLES=(
    "ods_campaign_product_subcategory_fpd"
    "ods_category_fpd"
    "ods_customer_fpd"
    "ods_customer_product_ratings_ipd"
    "ods_marketing_campaigns_fpd"
    "ods_orders_ipd"
    "ods_ordersitem_ipd"
    "ods_payment_method_fpd"
    "ods_product_fpd"
    "ods_returns_ipd"
    "ods_subcategory_fpd"
    "ods_supplier_fpd"
)

# Create External Table Directory
echo "Creating Hive external table locations on HDFS..."
for table in "${TABLES[@]}"; do
    hdfs dfs -mkdir -p "${HDFS_BASE_PATH}/${table}"
    hdfs dfs -chmod -R 777 ${HDFS_BASE_PATH}
    echo "Created: ${HDFS_BASE_PATH}/${table}"
done

# Create Avro Schema Directory
echo "Creating Schema directory on HDFS..."
hdfs dfs -mkdir -p "$SCHEMA_HDFS_PATH"
echo "Created: $SCHEMA_HDFS_PATH"

# Upload .avsc files to HDFS Schema directory
LOCAL_SCHEMA_DIR="./avro_schema"  # local avro schema

echo "Uploading .avsc files to HDFS..."
for file in "$LOCAL_SCHEMA_DIR"/*.avsc; do
    if [[ -f "$file" ]]; then
        filename=$(basename "$file")  # get the filename
        hdfs dfs -put -f "$file" "$SCHEMA_HDFS_PATH/$filename"
        hdfs dfs -chmod -R 777 "$SCHEMA_HDFS_PATH/$filename"
        echo "Uploaded: $file → $SCHEMA_HDFS_PATH/$filename"
    fi
done

echo "All external locations and schema files have been set up successfully!"
