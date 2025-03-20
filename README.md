![1](https://github.com/user-attachments/assets/5b98ca67-3770-4d4a-b444-ad8b70c40557)

# Enterprise-Grade Offline Data Warehouse Solution for E-Commerce

<p align="center">
  <a href="https://github.com/Smars-Bin-Hu/EComDWH-Pipeline/tree/main/src">
      <img src="https://img.shields.io/badge/project-source_code-green?style=for-the-badge&logo=github" alt="Sublime's custom image"/>
  </a>
  <a href="https://github.com/Smars-Bin-Hu/EComDWH-Pipeline?tab=readme-ov-file#-project-documents">
      <img src="https://img.shields.io/badge/project-all%20documents-red?style=for-the-badge&logo=github" image"/>
   </a>
</p>

<p align="center">
<img src="https://img.shields.io/badge/apache_spark-3.3.0-blue?style=plastic&logo=apachespark&logoSize=auto&color=white"/>
<img src="https://img.shields.io/badge/apache_hadoop-3.2.4-blue?style=plastic&logo=apachehadoop&logoColor=yellow&logoSize=auto&color=blue"/>
<img src="https://img.shields.io/badge/apache_hive-3.1.3-blue?style=plastic&logo=apachehive&logoColor=yellow&logoSize=auto&color=yellow"/>
<img src="https://img.shields.io/badge/python-3.12.9-blue?style=plastic&logo=python&logoColor=yellow&logoSize=auto&color=blue"/>
</p>


This project aims to build an enterprise-grade offline data warehouse solution based on e-commerce platform order data. By leveraging **Docker containers** to simulate a big data platform, it achieves a complete workflow from ETL processing to data warehouse modeling, OLAP analysis, and data visualization. 

The core value of this project lies in its implementation of **enterprise-grade data warehouse modeling**, integrating e-commerce order data with relevant business themes through standardized dimension modeling and fact table design, ensuring data accuracy, consistency, and traceability. Meanwhile, **the deployment of a big data cluster via Docker containers** simplifies environment management and operational costs, offering a flexible deployment model for distributed batch processing powered by Spark. Additionally, the project incorporates **CI/CD automation**, enabling rapid iterations while maintaining the stability and reliability of the data pipeline. Storage and computation are also **highly optimized** to maximize hardware resource utilization.

To monitor and manage the system effectively, a **Grafana-based cluster monitoring system** has been implemented, providing real-time insights into cluster health metrics and assisting in performance tuning and capacity planning. Finally, by integrating **business intelligence (BI) and visualization solutions**, the project transforms complex data warehouse analytics into intuitive dashboards and reports, allowing business teams to make data-driven decisions more efficiently.

By combining these critical features—including:
- Big Data Cluster Deployment
- Enterprise-Grade Data Warehouse Modeling Standard
- Distributed Batch Processing with Spark
- CI/CD Automation
- Optimized Storage & Computation
- Cluster Monitoring System using Grafana
- Business Intelligence & Visualization

this project delivers a professional, robust, and highly efficient solution for enterprises dealing with large-scale data processing and analytics.

## Key Features

### Tech Stack

This project sets up a high-availability big data platform, including the following components:

![Apache Spark](https://img.shields.io/badge/Spark-FDEE21?style=for-the-badge&logo=apachespark&logoColor=black) 	![Apache Hadoop](https://img.shields.io/badge/Hadoop-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=black) ![Apache Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Airflow&logoColor=white) ![Apache Hive](https://img.shields.io/badge/Hive-FDEE21?style=for-the-badge&logo=apachehive&logoColor=black)  ![ClickHouse](https://img.shields.io/badge/ClickHouse-FFCC01?style=for-the-badge&logo=clickhouse&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

| Components             | Features                 | Version |
|------------------------|--------------------------|---------|
| Apache Hadoop HDFS     | Distributed Data Storage | 3.2.4   |
| Apache Hadoop YARN     | Resource Management      | 3.2.4   |
| Apache Zookeeper       | High Availability        | 3.8.4   |
| Apache Spark           | Distributed Computing    | 3.3.0   |
| Apache Hive            | Data Warehousing         | 3.1.3   |
| Apache Airflow         | Workflow Scheduling      |         |
| Azure Cloud ClickHouse | OLAP Analysis            |         |
| Microsoft PowerBI      | BI Dashboard             |         |
| Prometheus             | Monitoring               |         |
| Grafana                | Monitoring GUI           |         |
| Docker                 | Containerization         |         |

### Project Key Features

| ✅ Feature | 🔥 Core Highlights | 📦 Deliverables |
|-----------|------------------|---------------|
| **1. Data Warehouse Modeling** | - Full dimensional modeling process (Star Schema / Snowflake Schema) <br> - Standardized development norms (ODS/DWD/DWM/DWS/ADS five-layer modeling) <br> - Business Matrix: defining & managing dimensions & fact tables | - Data warehouse design document (Markdown/PDF) <br> - Hive SQL modeling code <br> - Database ER diagram |
| **2. Cluster Deployment** | - Fully containerized deployment with Docker for quick replication <br> - High-availability environment: Hadoop + Hive + Spark + Zookeeper + ClickHouse | - Docker images (open-source Dockerfile) <br> - `.env` configuration file <br> - `docker-compose.yml` (one-click cluster startup) <br> - Infra configuration files (Hadoop, Hive, Spark, Zookeeper) |
| **3. Distributed Batch Processing** | - ETL processing using Spark for Oracle relational data <br> - Multi-layer processing: ODS → DWD → DWM → DWS → ADS <br> - Efficient data transformation & aggregation | - Spark ETL code (PySpark) <br> - SparkSQL scripts <br> - Data flow diagram |
| **4. CI/CD Automation** | - Automated Airflow DAG deployment (auto-sync with code updates) <br> - Automated Spark job submission (eliminates manual `spark-submit`) <br> - Hive table schema change detection (automatic alerts) | - GitHub Actions / Jenkins pipeline <br> - CI/CD documentation <br> - Sample log screenshots |
| **5. Storage & Computation Optimization** | - SQL optimization (dynamic partitioning, indexing, storage partitioning) <br> - Spark tuning: Salting, Skew Join Hint, Broadcast Join, `reduceByKey` vs. `groupByKey` <br> - Hive tuning: Z-Order sorting (boost ClickHouse queries), Parquet + Snappy compression | - Pre & post optimization performance comparison <br> - Spark optimization code <br> - SQL execution plan screenshots |
| **6. Monitoring** | - Prometheus + Grafana for monitoring Spark / Hive / ClickHouse <br> - ETL job status monitoring <br> - Data latency & failure rate tracking | - Prometheus configuration files <br> - Grafana dashboard screenshots <br> - ETL job monitoring logs |
| **7. Business Intelligence & Visualization** | - PowerBI dashboards for data analysis <br> - Real business-driven visualizations <br> - Providing actionable business insights | - PowerBI visualization screenshots <br> - Business analysis report <br> - Key business metric explanations (BI Insights) |

## 📁 Project Directory

```bash
/bigdata-datawarehouse-project
│── /docs                         # docs (all business and technologies documents about this project)
│── /src
    │── /data_pipeline            # data pipeline code (ETL/ELT Logic, output)
    │── /warehouse_modeling       # DWH modelling（Hive SQL etc.）
    │── /batch_processing         # Data Batch processing (PySpark + SparkSQL)
    │── /scheduler                # Task Scheduler(Airflow)
    │── /infra                    # infrastructure deployment(Docker, configuration files)
    │── /scripts                  # common used commands and scripts
    │── /README                   # Source Code Use Instruction Markdown Files
    │── README.md                 # Navigation of Source Code Use Instruction
    │── main_data_pipeline.py     # operate the data_pipeline module to do the `Extract` and `Load` jobs
    │── main_batch_processing.py  # operate the batch_processing module to do the `Transform` jobs
│── /tests                        # all small features unit testing scripts (DWH modelling, data pipeline, scheduler etc.) 
│── README.md                     # Introduction about project
│── docker-compose-bigdata.yml    # Docker Compose to launch the docker cluster
│── .env                          # `public the .env on purpose` for docker-compose file use
│── .gitignore                    # Git ignore some directory not to be committed to the remote repo
```

## 🔗 Quick Start `/src`

### [Source Code Use Instruction](./src/README.md)

####  [Quick Start](./src/README/quick-start.md)

### Data Pipeline
#### [Upstream ELT: OLTP to Data Warehouse](./src/README/spark-upstream.md)
#### [Downstream ELT: Data Warehouse to OLAP](./src/README/spark-downstream.md)

### Batch Processing

### Warehouse Modelling

### Automation Scheduler

## 🔗 Project Documents `/docs`

#### 1. Business logic && Tech Selection

- Business Logic
- [Project Tech Architecture](./docs/doc/tech-architecture.md)

#### 2. Data Warehouse Modelling

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

#### 3. Troubleshooting

  - [Future Bugs to Fix](./docs/doc/error-handling/future-fix.md)
  - [04_MAR_2025](./docs/doc/error-handling/04_MAR_2025.md)
  - [05_MAR_2025](./docs/doc/error-handling/05_MAR_2025.md)
  - [06_MAR_2025](./docs/doc/error-handling/06_MAR_2025.md)


#### 4. Infrastructure & Building

  - 核心架构docker容器分布图
  - Hadoop 3节点 的搭建和配置
  - Hive 节点的搭建和配置
  - Spark 节点的搭建和配置
  - mysql 节点的搭建和配置
  - oracle 节点的搭建和配置
  - airflow 节点的搭建和配置
  - `docker-compose` 文件的配置

#### 5. Development

  - Data Warehousing
    - ods
    - dwd
  - Data Pipeline ETL
    - Spark on Yarn to connect Oracle (Hello World)
    - Spark to extract data and load to HDFS
    - OOP
  - Scheduler (Airflow)
  - some files under /scripts

#### 6. Optimization

  - [Too many INFO logs: Reducing Spark Console Log Levels](./docs/doc/optimization/reducing-spark-console-log-levels.md)

#### 7. Testing
  - spark_connect_oracle.py  



