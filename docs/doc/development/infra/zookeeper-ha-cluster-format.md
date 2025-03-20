# Hadoop HA Cluster Initialize

**If first launching hadoop cluster,** we should initialize the cluster(e.g format the namenode)

Aiming at `hadoop-master`,`hadoop-worker1`,`hadoop-worker2`, initial hadoop metadata
```text
rm -rf $HADOOP_HOME/data/journal/ns-ha/*
rm -rf $HADOOP_HOME/data/data/*
rm -rf $HADOOP_HOME/data/name/*
```

Launch the hadoop cluster
```bash
# 1. All 3: `hadoop-master`,`hadoop-worker1`,`hadoop-worker2`
zkServer.sh start && hdfs --daemon start journalnode 
```

On the first NameNode `hadoop-master`, run
```bash
hdfs namenode -format
hdfs namenode -initializeSharedEdits
```
Choose N if encounter: `Re-format filesystem in QJM to [172.18.0.2:8485, 172.18.0.3:8485, 172.18.0.4:8485] ? (Y or N)`

On the first NameNode `hadoop-master`, run
```bash
hdfs --daemon start namenode  && hdfs --daemon start zkfc
```

On the second NameNode `hadoop-worker2` run, and load the metadata(edit, fsimage etc) in first namenode to second namenode
```bash
hdfs namenode -bootstrapStandby
```

On the first NameNode `hadoop-worker2`, run
```bash
hdfs --daemon start namenode  && hdfs --daemon start zkfc
```

aiming at `hadoop-master`,`hadoop-worker1`,`hadoop-worker2`
```bash
# 3. `hadoop-master`,`hadoop-worker1` (2 resourceManagers)
yarn --daemon start resourcemanager

# 4. All 3: `hadoop-master`,`hadoop-worker1`,`hadoop-worker2`
rm -rf /usr/local/opt/module/hadoop/data/data/* && hdfs --daemon start datanode && yarn --daemon start nodemanager

# 5. `hadoop-master` only
mr-jobhistory-daemon.sh start historyserver
```