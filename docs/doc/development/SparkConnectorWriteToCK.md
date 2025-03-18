# Connecting Spark to Azure Cloud ClickHouse: A Successful Integration Case

## Introduction
Integrating Apache Spark with ClickHouse for large-scale data processing can be challenging, especially when dealing with compatibility issues and dependency conflicts. This document provides a step-by-step guide to successfully connecting Spark 3.3.0 to Azure Cloud ClickHouse, reading Parquet data from Hive, and writing it to ClickHouse using the Spark ClickHouse Connector.

## Environment Details
- **Spark Version:** 3.3.0
- **Scala Version:** 2.12.15
- **JDK Version:** 1.8.0_442
- **ClickHouse:** Azure Cloud ClickHouse
- **Hive Storage Format:** Parquet

## Key Challenges and Solutions
During the setup, we encountered several issues, including `ClassNotFoundException`, missing dependencies, and incorrect connection configurations. Below are the key takeaways:

1. **Ensure Compatibility Between Dependencies**
    - The Spark ClickHouse connector and ClickHouse JDBC driver must be compatible. Based on the official [ClickHouse compatibility matrix](https://clickhouse.com/docs/integrations/apache-spark/spark-native-connector#compatibility-matrix), the following versions were used:
        - Spark Connector: `clickhouse-spark-runtime-3.3_2.12:0.8.0`
        - ClickHouse JDBC Driver: `clickhouse-client:0.6.3`
    - Using the wrong versions caused missing class errors and failed connections.

2. **Avoid Using Deprecated Connection Methods**
    - Traditional connection methods like `df.write().format("clickhouse")` resulted in `ClassNotFoundException` due to the removal of `DefaultSource` class.
    - Instead, we used Spark’s catalog-based configuration to manage ClickHouse connections.

## Installation and Setup

### 1. Configure Spark Dependencies
#### Option 1: Using `--jars`
Download and place compatible JAR files in `/opt/spark/jars/`:
```
/opt/spark/jars/com.clickhouse.spark_clickhouse-spark-runtime-3.3_2.12-0.8.0.jar
/opt/spark/jars/com.clickhouse_clickhouse-client-0.6.3.jar
/opt/spark/jars/com.clickhouse_clickhouse-http-client-0.6.3.jar
/opt/spark/jars/org.apache.httpcomponents.client5_httpclient5-5.2.1.jar
/opt/spark/jars/com.clickhouse_clickhouse-data-0.6.3.jar
/opt/spark/jars/org.apache.httpcomponents.core5_httpcore5-5.2.jar
/opt/spark/jars/org.apache.httpcomponents.core5_httpcore5-h2-5.2.jar
/opt/spark/jars/org.slf4j_slf4j-api-1.7.36.jar
```

#### Option 2: Using `--packages`
Alternatively, use Maven dependencies to download the required JARs dynamically:
```
spark-submit --master yarn \
    --deploy-mode client \
    --driver-memory 512m \
    --executor-memory 1g \
    --executor-cores 1 \
    --num-executors 1 \
    --conf "spark.executor.memoryOverhead=512" \
    --conf "spark.executor.memoryOverhead=256" \
    --conf spark.hadoop.yarn.log-aggregation.wait.ms=60000 \
    --conf spark.eventLog.enabled=true \
    --conf spark.eventLog.dir=hdfs:///spark-logs \
    --packages com.clickhouse.spark:clickhouse-spark-runtime-3.3_2.12:0.8.0,com.clickhouse:clickhouse-client:0.6.3,com.clickhouse:clickhouse-http-client:0.6.3,org.apache.httpcomponents.client5:httpclient5:5.2.1 \
    /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/test/unit_test/data_pipeline/spark_hive_to_clickhouse.py
```

## Code Implementation

```python
from pyspark.sql import SparkSession

clickhouse_host = "vm9roqk7je.westus3.azure.clickhouse.cloud"
clickhouse_port = "8443"  # HTTPS port
clickhouse_db = "ads_data_mart_ecomerce"
clickhouse_table = "ads_orders_detailed_info_wide_ipd"
clickhouse_user = "default"
clickhouse_password = "******"

spark = SparkSession.builder \
    .appName("Spark to Azure Cloud CK ADS - JDBC") \
    .getOrCreate()

# Read Hive Parquet Data
path_to_hdfs_parquet = "/user/hive/warehouse/dws/dws_orders_detailed_info_wide_ipd/data_date=2025-03-10/part-00000-24c51043-df4f-46af-87fc-b1034cdc2db1.c000.snappy.parquet"
df = spark.read.parquet(f"hdfs://ns-ha{path_to_hdfs_parquet}")

# Configure ClickHouse Connection
spark.conf.set("spark.sql.catalog.clickhouse", "com.clickhouse.spark.ClickHouseCatalog")
spark.conf.set("spark.sql.catalog.clickhouse.host", clickhouse_host)
spark.conf.set("spark.sql.catalog.clickhouse.protocol", "https")
spark.conf.set("spark.sql.catalog.clickhouse.http_port", clickhouse_port)
spark.conf.set("spark.sql.catalog.clickhouse.user", clickhouse_user)
spark.conf.set("spark.sql.catalog.clickhouse.password", clickhouse_password)
spark.conf.set("spark.sql.catalog.clickhouse.database", clickhouse_db)
spark.conf.set("spark.sql.catalog.clickhouse.option.ssl", "true")
spark.conf.set("spark.clickhouse.write.format", "json")

# Write Data to ClickHouse
df.writeTo(f"clickhouse.{clickhouse_db}.{clickhouse_table}").append()

spark.stop()
```

## Conclusion
This guide demonstrates a reliable method to connect Spark to Azure Cloud ClickHouse and efficiently process large datasets from Hive. The key takeaways include:
1. **Using compatible dependencies** as per the ClickHouse official compatibility matrix.
2. **Avoiding deprecated connection methods** and utilizing Spark catalog-based connections.
3. **Leveraging both `--jars` and `--packages` approaches** for dependency management.
4. **Ensuring SSL connection** for secure communication with Azure Cloud ClickHouse.

By following this approach, we successfully overcame `ClassNotFoundException` errors and established a stable integration between Spark and ClickHouse.