# Optimization: Reducing Spark Console Log Levels

> Edited By: Smars Hu
> Date: 05 Mar 2025

## **Scenario**

When running Spark jobs in **client mode**, the console output is often flooded with excessive log messages, especially at the `INFO` level. This makes it difficult to locate the actual computation results among the logs.

## **Root Cause**

By default, Spark logs are set to `INFO` level, which means a large number of system messages (such as execution plans, resource allocation, and memory usage) are printed to the console. While these logs are useful for debugging, they can overwhelm the output when trying to focus on job results.

## **Optimization Methods**

### **Method 1: Modify `log4j.properties` to Reduce Logging**

Edit the Spark `log4j.properties` file to change the root log level from `INFO` to `ERROR`.

1. Change `log4j.properties` file in Spark configuration folder:
   ```properties
   log4j.rootCategory=ERROR, console
   ```
2. Save and restart Spark to apply changes.

### **Method 2: Set Log Level in the Spark Application Code (Recommend)**

You can dynamically change the log level within your PySpark script:

```python
from pyspark.sql import SparkSession
import logging

# Create Spark session
spark = SparkSession.builder.appName("ReduceLogLevel").getOrCreate()

# Reduce log level to ERROR
spark.sparkContext.setLogLevel("ERROR")
logging.basicConfig(level=logging.ERROR)
```

### **Method 3: Configure Logging in `spark-submit`**

You can override the log level when submitting a job using `spark-submit`:

```shell
spark-submit \
    --master yarn \
    --deploy-mode client \
    --conf "spark.driver.extraJavaOptions=-Dlog4j.rootCategory=ERROR,console" \
    your_script.py
```

