# Start
# 1. All
zkServer.sh start
hdfs --daemon start journalnode 

# 2. Master and worker2 (NameNode)
hdfs --daemon start namenode 
hdfs --daemon start zkfc

# 3. Master and worker1 (resourceManager)
yarn --daemon start resourcemanager

# 4. All
rm -rf /usr/local/opt/module/hadoop/data/data/current/in_use.lock  # in case the lock is existing because of invalid exiting last time
hdfs --daemon start datanode
yarn --daemon start nodemanager


# Stop
# 1. All
yarn --daemon stop nodemanager
hdfs --daemon stop datanode

# 2. Master and worker1 (resourceManager)
yarn --daemon stop resourcemanager

# 3. Master and worker2 (NameNode)
hdfs --daemon stop zkfc # all stop this first 
# after stop zkfc, stop NN
hdfs --daemon stop namenode 

# 4. All
hdfs --daemon stop journalnode
zkServer.sh stop

# Check
jps

# standby & active
hdfs haadmin -getServiceState nn1 # name node
hdfs haadmin -getServiceState nn2
yarn rmadmin -getServiceState rm1 # resource manager
yarn rmadmin -getServiceState rm2 

yarn node -list # nodemanager

