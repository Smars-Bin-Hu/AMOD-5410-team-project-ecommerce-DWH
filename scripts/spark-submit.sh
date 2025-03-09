conda activate pyspark_env
# pyspark --master yarn --deploy-mode client

# cluster mode - for testing
spark-submit --master yarn \
    --deploy-mode cluster \
    --driver-memory 512m \
    --executor-memory 1g \
    --executor-cores 1 \
    --num-executors 1 \
    --jars /opt/spark/jars/ojdbc8.jar \
    --conf "spark.yarn.executor.memoryOverhead=512" \
    --conf "spark.yarn.driver.memoryOverhead=256" \
    --conf "spark.driver.extraClassPath=/opt/spark/jars/ojdbc8.jar" \
    --conf spark.hadoop.yarn.log-aggregation.wait.ms=60000 \
    --conf spark.eventLog.enabled=true \
    --conf spark.eventLog.dir=hdfs:///spark-logs \
    /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/data_pipeline/unit_test/spark_connect_oracle.py

# client mode - for testing
spark-submit --master yarn \
    --deploy-mode client \
    --driver-memory 512m \
    --executor-memory 1g \
    --executor-cores 1 \
    --num-executors 1 \
    --jars /opt/spark/jars/ojdbc8.jar \
    --conf "spark.yarn.executor.memoryOverhead=512" \
    --conf "spark.yarn.driver.memoryOverhead=256" \
    --conf "spark.driver.extraClassPath=/opt/spark/jars/ojdbc8.jar" \
    --conf spark.hadoop.yarn.log-aggregation.wait.ms=60000 \
    --conf spark.eventLog.enabled=true \
    --conf spark.eventLog.dir=hdfs:///spark-logs \
    --packages org.apache.spark:spark-avro_2.12:3.3.0\
    /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/test/unit_test/data_pipeline/spark_load_to_hive.py

# final spark submit python proejct package, otherwise the spark cannot regconize the package while importing
spark-submit --master yarn \
    --deploy-mode client \
    --driver-memory 512m \
    --executor-memory 1g \
    --executor-cores 1 \
    --num-executors 1 \
    --jars /opt/spark/jars/ojdbc8.jar \
    --conf "spark.executor.memoryOverhead=512" \
    --conf "spark.executor.memoryOverhead=256" \
    --conf "spark.driver.extraClassPath=/opt/spark/jars/ojdbc8.jar" \
    --conf spark.hadoop.yarn.log-aggregation.wait.ms=60000 \
    --conf spark.eventLog.enabled=true \
    --conf spark.eventLog.dir=hdfs:///spark-logs \
    --packages org.apache.spark:spark-avro_2.12:3.3.0\
    --py-files /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/data_pipeline.zip \
    /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/main.py


    
