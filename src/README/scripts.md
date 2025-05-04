# /src/scripts

## Cluster Shell Scripts Directory Structure

The `scripts/` directory contains modular shell scripts for starting and stopping key services in a containerized or distributed big data infrastructure. Each subdirectory corresponds to a service or role-based node group.

```text
scripts/
├── airflow/
│   ├── start-airflow.sh                    # Start Airflow webserver & scheduler
│   └── stop-airflow.sh                     # Stop Airflow services
│
├── hadoop-master/
│   ├── my-start-historyserver.sh           # Start Hadoop history server
│   ├── my-start-NM-DN.sh                   # Start NodeManager + DataNode (if co-located)
│   ├── my-start-NN-ZKFC.sh                 # Start NameNode with ZK Failover Controller
│   ├── my-start-node-exporter.sh           # Start Prometheus node_exporter
│   ├── my-start-RM.sh                      # Start ResourceManager
│   ├── my-start-zk.sh                      # Start ZooKeeper service
│   ├── my-stop-hadoop-cluster.sh           # Stop all master Hadoop services
│   └── my-stop-node-exporter.sh            # Stop node_exporter
│
├── hadoop-worker1/
│   ├── my-start-NM-DN.sh                   # Start NodeManager + DataNode (if co-located)
│   ├── my-start-node-exporter.sh           # Start Prometheus node_exporter
│   ├── my-start-RM.sh                      # Start ResourceManager
│   ├── my-start-zk.sh                      # Start ZooKeeper service
│   ├── my-stop-hadoop-cluster.sh           # Stop all worker Hadoop services
│   └── my-stop-node-exporter.sh            # Stop node_exporter
│
├── hadoop-worker2/
│   ├── my-start-NM-DN.sh                   # Start NodeManager + DataNode (if co-located)
│   ├── my-start-NN-ZKFC.sh                 # Start NameNode with ZK Failover Controller
│   ├── my-start-node-exporter.sh           # Start Prometheus node_exporter
│   ├── my-start-zk.sh                      # Start ZooKeeper service
│   ├── my-stop-hadoop-cluster.sh           # Stop all worker Hadoop services
│   └── my-stop-node-exporter.sh            # Stop node_exporter
│
├── hive/
│   ├── start-hive-services.sh              # Start HiveServer2, Metastore, etc.
│   └── stop-hive-services.sh               # Stop Hive services
│
├── monitoring/
│   ├── start-monitoring-services.sh        # Start Prometheus, Grafana, Alertmanager
│   └── stop-monitoring-services.sh         # Stop monitoring services
│
├── mysql-hive-metastore/
│   ├── dump-mysql.sh                       # Export MySQL DB (Hive Metastore)
│   ├── restore-mysql.sh                    # Restore MySQL DB
│   ├── start-mysqld-exporter.sh            # Start MySQL exporter for Prometheus
│   └── stop-mysqld-exporter.sh             # Stop MySQL exporter
│
└── spark/
    ├── start-spark-services.sh             # Start Spark History Server, etc.
    └── stop-spark-services.sh              # Stop Spark services
```

Notes:

- Each script is typically intended to be executed inside its corresponding container or host.

- `node-exporter` scripts are used for Prometheus-based monitoring.

- Scripts follow a convention of `start-*` and `stop-*` for easy service lifecycle management.

- Master and worker nodes have independently defined service startup scripts to simulate a real distributed Hadoop cluster.

