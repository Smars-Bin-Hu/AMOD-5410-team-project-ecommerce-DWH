# hadoop master
zkServer.sh start
hdfs --daemon start journalnode 

# Master and worker2 (NameNode)
hdfs --daemon start namenode 
hdfs --daemon start zkfc

# Master and worker1 (resourceManager)
yarn --daemon start resourcemanager

# All
rm -rf /usr/local/opt/module/hadoop/data/data/current/in_use.lock
hdfs --daemon start datanode
yarn --daemon start nodemanager






# Check
jps

# standby & active
hdfs haadmin -getServiceState nn1 # name node
hdfs haadmin -getServiceState nn2
yarn rmadmin -getServiceState rm1 # resource manager
yarn rmadmin -getServiceState rm2 

yarn node -list # nodemanager

