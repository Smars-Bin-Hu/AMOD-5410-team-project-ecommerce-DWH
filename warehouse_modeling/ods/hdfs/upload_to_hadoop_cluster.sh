#!/bin/bash

PORT="2222"
USERNAME="root"
HOSTNAME="localhost"
LOCAL_UPLOADED_FILES="../avro_schema ./hdfs_ods_env_initial.sh"
TARGET_PATH="/usr/local/downloads/hive_ods_avro_schema_configs"


# upload /avro_schema/*.avsc and hdfs_ods_env_initial.sh to Hadoop Cluster(NameNode)
scp -P ${PORT} -r ${LOCAL_UPLOADED_FILES} ${USERNAME}@${HOSTNAME}:${TARGET_PATH}