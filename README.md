# AMOD-5410-team-project-ecommerce-DWH

## 📖 Introduction

**Name:**

**Background:**

**Goal:** To build a data batch processing datawarehouse,including data ingestion, cleaning, storage, modelling, analytis and scheduler. Use tech stach as below.

## 🚀 Tech Stack

- **Data Source(OLTP):** Oracle Database
- **Data Extraction, Load:** Airflow + JDBC or Apache Sqoop
- **Data Storage and Resources Management:** Apache Hadoop(HDFS, Yarn)
- **Data Warehousing:** Apache Hive, MySQL(Metastore), Dimension Modelling
- **Data Transform:** Apache Spark(PySpark), SparkSQL
- **Scheduler:** Airflow
- **OLAP engine:** MySQL or clickhouse
- **Data Application Layer**: PowerBI or tableau

## 📁 Project Directory

```bash
/bigdata-datawarehouse-project
│── /docs                    # docs (technologies architecture diagram, desgin, README)
│── /data_pipeline           # data pipeline code (ETL/ELT Logic, output)
│── /warehouse_modeling      # DWH modelling（Hive/SparkSQL etc.）
│── /batch_processing        # Data Batch processing (Hadoop, Hive, Spark)
│── /scheduler               # Task Scheduler(Airflow/DolphinScheduler)
│── /infra                   # infrastructure deployment(Docker, Kubernetes)
│── /notebooks               # Jupyter Notebook
│── /tests                   # Testing code
│── /scripts                 # deployment and operations script and command
│── README.md                # Introduction about project
│── docker-compose.yml       # Docker Compose to launch the project
│── requirements.txt         # Python dependencies
```

## 💪 Quick Start


Add hosts to your local `/etc/hosts`

```
# for docker network
127.0.0.1   hadoop-master 
127.0.0.1   hadoop-worker1
127.0.0.1   hadoop-worker2
127.0.0.1   mysql-hive-metastore
127.0.0.1   hive
127.0.0.1   spark
127.0.0.1   oracle-oltp
```
