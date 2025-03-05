# Start
# 1. All
zkServer.sh start && hdfs --daemon start journalnode 

# 2. Master and worker2 (NameNode)
hdfs --daemon start namenode  && hdfs --daemon start zkfc

# 3. Master and worker1 (resourceManager)
yarn --daemon start resourcemanager

# 4. All
rm -rf /usr/local/opt/module/hadoop/data/data/current/in_use.lock  && hdfs --daemon start datanode && yarn --daemon start nodemanager

# 5. Master
mr-jobhistory-daemon.sh start historyserver


# Stop
# 0. Master
mr-jobhistory-daemon.sh stop historyserver

# 1. All
stop-yarn.sh && stop-dfs.sh && hdfs --daemon stop journalnode && zkServer.sh stop






# Check
jps

# standby & active
hdfs haadmin -getServiceState nn1 # name node
hdfs haadmin -getServiceState nn2
yarn rmadmin -getServiceState rm1 # resource manager
yarn rmadmin -getServiceState rm2 

yarn node -list # nodemanager

