Hadoop HA Cluster Launching 

## Launching Services

1. step 1: all 3 containers
```bash 
zkServer.sh start && hdfs --daemon start journalnode 
```

2. step2: `Master` and `worker2` (NameNode)
```bash
hdfs --daemon start namenode  && hdfs --daemon start zkfc
```

3. step3: `Master` and `worker1` (resourceManager)
```bash
yarn --daemon start resourcemanager
```

4. step4: all 3 containers
```bash
rm -rf /usr/local/opt/module/hadoop/data/data/current/in_use.lock && hdfs --daemon start datanode && yarn --daemon start nodemanager
```

5. step5: `Master` only
```bash
mr-jobhistory-daemon.sh start historyserver
```

## Stop Services

1. step 1: `Master` only
```bash
mr-jobhistory-daemon.sh stop historyserver
```

2. step 2: all 3 containers
```bash
stop-yarn.sh && stop-dfs.sh && hdfs --daemon stop journalnode && zkServer.sh stop
```

## Check the status

all three containers, could run `jps`
```bash
jps
```

standby & active NN and RM
```bash
hdfs haadmin -getServiceState nn1
hdfs haadmin -getServiceState nn2
yarn rmadmin -getServiceState rm1
yarn rmadmin -getServiceState rm2 
```

```bash
hdfs datanode -list
yarn node -list  nodemanager
```
