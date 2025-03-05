conda activate pyspark_env
pyspark --master yarn --deploy-mode client

# 局部覆盖
# 本次命令，不读取当前环境下的PYSPARK_PYTHON，保证发送到nodemanager的时候，
# 可以读取 NM上的PYSPARK_PYTHON=/usr/bin/python3.8
# 而不是 /opt/miniconda3/envs/pyspark_env/bin/python
env -i \
    PYSPARK_PYTHON=/usr/bin/python3.8 \
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
    /opt/miniconda3/envs/pyspark_env/jobs_sync/Users/smars/Developer/big-data-engineering-project1/data_pipeline/unit_test/spark_connect_oracle.py
