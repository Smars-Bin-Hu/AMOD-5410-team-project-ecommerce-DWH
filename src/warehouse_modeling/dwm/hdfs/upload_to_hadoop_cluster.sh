#!/bin/bash

PORT="2222"
USERNAME="root"
HOSTNAME="localhost"
LOCAL_UPLOADED_FILES="./hdfs_dwm_env_initial.sh"
TARGET_PATH="/usr/local/downloads/hive_dwm_sh_script"

# upload hdfs_ods_env_initial.sh to Hadoop Cluster(HDFS)
scp -P ${PORT} -r ${LOCAL_UPLOADED_FILES} ${USERNAME}@${HOSTNAME}:${TARGET_PATH}