from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
import clickhouse_connect


clickhouse_host = "vm9roqk7je.westus3.azure.clickhouse.cloud"
clickhouse_port = "8443"  # HTTPS Port
clickhouse_db = "ads_data_mart_ecomerce"
clickhouse_table = "ads_orders_detailed_info_wide_ipd"
clickhouse_user = "default"
clickhouse_password = "8h2Dpa6Y_pl07" # for testing
# jdbc_url = f"jdbc:clickhouse://{clickhouse_host}:{clickhouse_port}/{clickhouse_db}?ssl=true"
# jdbc_driver = "com.clickhouse.jdbc.ClickHouseDriver"

spark = SparkSession.builder \
    .appName("Spark to Azure Cloud CK ADS - JDBC") \
    .getOrCreate()

# Read Hive Parquet File
# spark.read.parquet() cannot get the partition field, so NOT recommend this.
# use the Spark SQL instead
df = spark.sql("select * from dws.dws_orders_detailed_info_wide_ipd;")
df.show()

# partition field processing
# in the ck, the data_date is `Date` data type
# in the hive, the data_date type is String
# so because the mismatch of data type, ck will parse the data as default timestamp '1970-01-01'
df = df.withColumn("data_date", to_date(col("data_date")))  # make sure this is DateType

spark.conf.set("spark.sql.catalog.clickhouse", "com.clickhouse.spark.ClickHouseCatalog")
spark.conf.set("spark.sql.catalog.clickhouse.host", clickhouse_host)
spark.conf.set("spark.sql.catalog.clickhouse.protocol", "https")
spark.conf.set("spark.sql.catalog.clickhouse.http_port", clickhouse_port)
spark.conf.set("spark.sql.catalog.clickhouse.user", clickhouse_user)
spark.conf.set("spark.sql.catalog.clickhouse.password", clickhouse_password)
spark.conf.set("spark.sql.catalog.clickhouse.database", clickhouse_db)
spark.conf.set("spark.sql.catalog.clickhouse.option.ssl", "true")
spark.conf.set("spark.clickhouse.write.format", "json")

df.writeTo(f"clickhouse.{clickhouse_db}.{clickhouse_table}").append()

spark.stop()

"""
Based on Jars on the Spark Driver Container under $SPARK_HOME/jars
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
    --jars /opt/spark/jars/com.clickhouse.spark_clickhouse-spark-runtime-3.3_2.12-0.8.0.jar,/opt/spark/jars/com.clickhouse_clickhouse-client-0.6.3.jar,/opt/spark/jars/com.clickhouse_clickhouse-http-client-0.6.3.jar,/opt/spark/jars/org.apache.httpcomponents.client5_httpclient5-5.2.1.jar,/opt/spark/jars/com.clickhouse_clickhouse-data-0.6.3.jar,/opt/spark/jars/org.apache.httpcomponents.core5_httpcore5-5.2.jar,/opt/spark/jars/org.apache.httpcomponents.core5_httpcore5-h2-5.2.jar,/opt/spark/jars/org.slf4j_slf4j-api-1.7.36.jar \
    /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/test/unit_test/data_pipeline/spark_hive_to_clickhouse.py

Based on Maven Repo 
 spark-submit --master yarn \
     --deploy-mode client \
     --driver-memory 512m \
     --executor-memory 1g \
     --executor-cores 1  \
     --num-executors 1 \
     --conf "spark.executor.memoryOverhead=512" \
     --conf "spark.executor.memoryOverhead=256" \
     --conf spark.hadoop.yarn.log-aggregation.wait.ms=60000 \
     --conf spark.eventLog.enabled=true \
     --conf spark.eventLog.dir=hdfs:///spark-logs \
     --packages com.clickhouse.spark:clickhouse-spark-runtime-3.3_2.12:0.8.0,com.clickhouse:clickhouse-client:0.6.3,com.clickhouse:clickhouse-http-client:0.6.3,org.apache.httpcomponents.client5:httpclient5:5.2.1 \
     /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/test/unit_test/data_pipeline/spark_hive_to_clickhouse.py
"""
#%%
