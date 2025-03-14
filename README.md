# AMOD-5410-team-project-ecommerce-DWH

## 📖 Introduction

**Name:**

**Background:**

**Goal:** To build a data batch processing datawarehouse, including data ingestion, cleaning, storage, modelling, analytis and scheduler. Use tech stach as below.

## 🚀 Tech Stack

- **Data Source(OLTP):** Oracle
- **Data Extraction, Load:** Airflow + JDBC
- **Data Storage and Resources Management:** HDFS, Yarn
- **Data Warehousing:** Apache Hive, MySQL(Metastore), Dimension Modelling
- **Data Transform:** PySpark, SparkSQL
- **Scheduler:** Airflow
- **OLAP engine:** clickhouse
- **Data Application Layer**: PowerBI

## 📁 Project Directory

```bash
/bigdata-datawarehouse-project
│── /docs                    # docs (all business and technologies documents about this project)
│── /src
    │── /data_pipeline       # data pipeline code (ETL/ELT Logic, output)
    │── /warehouse_modeling  # DWH modelling（Hive/SparkSQL etc.）
    │── /batch_processing    # Data Batch processing (Hadoop, Hive, Spark)
    │── /scheduler           # Task Scheduler(Airflow/DolphinScheduler)
    │── /infra               # infrastructure deployment(Docker, configuration)
    │── /scripts             # deployment and operations script and command
    │── main.py              # all python program entrance 
│── /tests                   # Testing code
│── README.md                # Introduction about project
│── docker-compose.yml       # Docker Compose to launch the project
│── .env                     # (ignored by git) Docker Compose to read the constant variable about environment
│── .gitignore               # Git ignore some directory to commit to the remote repo
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
127.0.0.1   airflow
```

## 📌 Project Documents

#### Business logic && Tech Selection

- Business Logic
- [Project Tech Architecture](./docs/doc/tech-architecture.md)

#### Data Warehouse Modelling

[DWH Modelling Standard Operation Procedure (SOP)](./docs/doc/dwh-modelling-sop.md)

- [Business Data Research](./docs/doc/business_data_research.md)
- Data Warehouse Development Specification
  - [Data Warehouse Layering Specification](./docs/doc/data-warehouse-development-specification/data-warehouse-layering-specification.md)
  - [Table Naming Conventions](./docs/doc/data-warehouse-development-specification/table-naming-convertions.md)
  - [Data Warehouse Column Naming Conventions](./docs/doc/data-warehouse-development-specification/partitioning-column-naming-conventions.md)
  - [Data Table Lifecycle Management Specification](./docs/doc/data-warehouse-development-specification/data-table-lifecycle-management-specification.md)

- Python Development Specification
  - Package Modulize
 
- SQL Development Specification
  - [Development Specification](./docs/doc/data-warehouse-development-specification/development-specification.md)

#### Troubleshooting

  - [Future Bugs to Fix](./docs/doc/error-handling/future-fix.md)
  - [04_MAR_2025](./docs/doc/error-handling/04_MAR_2025.md)
  - [05_MAR_2025](./docs/doc/error-handling/05_MAR_2025.md)
  - [06_MAR_2025](./docs/doc/error-handling/06_MAR_2025.md)


#### Infrastructure & Building

  - 核心架构docker容器分布图
  - Hadoop 3节点 的搭建和配置
  - Hive 节点的搭建和配置
  - Spark 节点的搭建和配置
  - mysql 节点的搭建和配置
  - oracle 节点的搭建和配置
  - airflow 节点的搭建和配置
  - `docker-compose` 文件的配置

#### Development

  - Data Warehousing
    - ods
    - dwd
  - datapipe ETL
    - Spark on Yarn to connect Oracle (Hello World)
    - Spark to extract data and load to HDFS
    - OOP
  - Scheduler (Airflow)
  - some files under /scripts

#### Optimization

  - [Too many INFO logs: Reducing Spark Console Log Levels](./docs/doc/optimization/reducing-spark-console-log-levels.md)

#### Testing
  - spark_connect_oracle.py  



