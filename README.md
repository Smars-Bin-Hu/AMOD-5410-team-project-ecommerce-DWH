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

| ✅ Feature | 🔥 Core Highlights | 📦 Deliverables |
|-----------|------------------|---------------|
| **1. Data Warehouse Modeling** | - Full dimensional modeling process (Star Schema / Snowflake Schema) <br> - Standardized development norms (ODS/DWD/DWM/DWS/ADS five-layer modeling) <br> - Business Matrix: defining & managing dimensions & fact tables | - Data warehouse design document (Markdown/PDF) <br> - Hive SQL modeling code <br> - Database ER diagram |
| **2. Cluster Deployment** | - Fully containerized deployment with Docker for quick replication <br> - High-availability environment: Hadoop + Hive + Spark + Zookeeper + ClickHouse | - Docker images (open-source Dockerfile) <br> - `.env` configuration file <br> - `docker-compose.yml` (one-click cluster startup) <br> - Infra configuration files (Hadoop, Hive, Spark, Zookeeper) |
| **3. Distributed Batch Processing** | - ETL processing using Spark for Oracle relational data <br> - Multi-layer processing: ODS → DWD → DWM → DWS → ADS <br> - Efficient data transformation & aggregation | - Spark ETL code (PySpark) <br> - SparkSQL scripts <br> - Data flow diagram |
| **4. CI/CD Automation** | - Automated Airflow DAG deployment (auto-sync with code updates) <br> - Automated Spark job submission (eliminates manual `spark-submit`) <br> - Hive table schema change detection (automatic alerts) | - GitHub Actions / Jenkins pipeline <br> - CI/CD code and documentation <br> - Sample log screenshots |
| **5. Storage & Computation Optimization** | - SQL optimization (dynamic partitioning, indexing, storage partitioning) <br> - Spark tuning: Salting, Skew Join Hint, Broadcast Join, `reduceByKey` vs. `groupByKey` <br> - Hive tuning: Z-Order sorting (boost ClickHouse queries), Parquet + Snappy compression | - Pre & post optimization performance comparison <br> - Spark optimization code <br> - SQL execution plan screenshots |
| **6. DevOps - Monitoring and Alerting** | - Prometheus + Grafana for performance monitoring Hadoop Cluster / MySQL <br> - AlertManager for alerting and email receiving | - Prometheus, Grafana configuration files <br> - Grafana dashboard screenshots <br> |
| **7. Business Intelligence & Visualization** | - PowerBI dashboards for data analysis <br> - Real business-driven visualizations <br> - Providing actionable business insights | - PowerBI visualization screenshots <br> - Business analysis report <br> - Key business metric explanations (BI Insights) |

this project delivers a professional, robust, and highly efficient solution for enterprises dealing with large-scale data processing and analytics.

## ⚙️ Core Deliverables

### 1. Data Warehouse Modeling
[🔗 Doc - Data Warehouse Modelling Specification](https://github.com/Smars-Bin-Hu/EComDWH-Pipeline?tab=readme-ov-file#2-data-warehouse-modelling)

![image](https://github.com/user-attachments/assets/ec924ea9-1acf-48a3-99ba-1546c1e8c3a9)
<p align="center"><em>Figure 1: DWH Dimensional Modelling SOP</em></p>

![image](https://github.com/user-attachments/assets/ab21c750-052f-4c10-baf0-bc97e5ed8274)
<p align="center"><em>Figure 2: DWH Dimensional Modelling Methodology Diagram</em></p>

![ECom-DWH-Pipeline](https://github.com/Smars-Bin-Hu/my-draw-io/blob/main/ECom-DWH-Datapipeline-Proejct/ECom-DWH-Pipeline.drawio.svg)
<p align="center"><em>Figure 3: DWH Dimensional Modelling Architecture</em></p>

### 2. Cluster Deployment

![ECom-DWH-Pipeline](https://github.com/Smars-Bin-Hu/my-draw-io/blob/main/ECom-DWH-Datapipeline-Proejct/ECom-DWH-Tech-Arc.drawio.svg)
<p align="center"><em>Figure 1: Data Platform Architecture</em></p>

[Docker Images GHCR](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/pkgs/container/proj1-dwh-cluster)

[Docker Compose File](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docker-compose-bigdata.yml)

### 3. Distributed Batch Processing

### 4. CI/CD Automation

<a href="https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/actions/workflows/main.yml">
    <img src="https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/actions/workflows/main.yml/badge.svg" image"/>
</a>

1. GitHub Actions Code

[workflows.main YAML](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/.github/workflows/main.yml)

2. Key Screenshots

<img width="1500" alt="image" src="https://github.com/user-attachments/assets/00fc170c-14ae-4f9d-a7e1-1480cb4d0112" />
<p align="center"><em>Figure 1: Data platform launching and stop automation</em></p>

<img width="1500" alt="image" src="https://github.com/user-attachments/assets/4a0a07fe-a629-4a10-a232-b01e0ed3aed2" />
<p align="center"><em>Figure 2: Sample Log Screenshot I </em></p>

<img width="1500" alt="image" src="https://github.com/user-attachments/assets/4c79ca68-286d-4f19-88a6-9917b565bc9e" />
<p align="center"><em>Figure 3: Sample Log Screenshot II </em></p>

3. [Automation Workflow](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/actions)

### 5. Storage & Computation Optimization

### 6. Monitoring

1. Code

[Monitoring Services Configuaration Files: Prometheus, Grafana, AlertManager](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main/src/infra/monitoring-config)

[Monitoring Services Start&Stop Scripts: Prometheus, Grafana, AlertManager](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main/src/scripts/monitoring)

[Container Metrics Exporter Start&Stop Scripts: `my-start-node-exporter.sh` & `my-stop-node-exporter.sh`](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main/src/scripts/hadoop-master)

2. Screenshots

<img width="1500" alt="Prometheus" src="https://github.com/user-attachments/assets/2f157fd1-1e41-4090-9c74-0fc3e97e385e" />
<p align="center"><em>Figure 1: Prometheus</em></p>
<img width="1501" alt="Grafana-Hadoop-Cluster-instance-hadoop-master" src="https://github.com/user-attachments/assets/7c4d94ca-3262-46be-adb3-18c3777a314f" />
<p align="center"><em>Figure 2: Grafana-Hadoop-Cluster-instance-hadoop-master</em></p>
<img width="1495" alt="Grafana-MySQLD" src="https://github.com/user-attachments/assets/7df991be-3642-4ad4-9672-3d8483423178" />
<p align="center"><em>Figure 3: Grafana-MySQLD</em></p>

### 7. Business Intelligence & Visualization

Use Microsoft PowerBI connect to the Clickhouse and extract the **analytical data storage** layer
<img width="1500" alt="image" src="https://github.com/user-attachments/assets/21eaea88-0fac-488d-9696-3be5720b4ac3" />
<p align="center"><em>Figure 1: PowerBI Dashboard Demo</em></p>

[PowerBI Public Access(Expirable)](https://app.powerbi.com/view?r=eyJrIjoiMzVjYTQ3NmMtODllZS00N2JhLWFkNWItMWI4MmYyNDZjMDc1IiwidCI6IjI0MGI3OWM1LTZiZWYtNDYwOC1hNDE3LTY1NjllODQzNTQ1YyJ9)

## Tech Stack

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
    │── /snippets                  # common used commands and snippets
    │── /README                   # Source Code Use Instruction Markdown Files
    │── README.md                 # Navigation of Source Code Use Instruction
    │── main_data_pipeline.py     # operate the data_pipeline module to do the `Extract` and `Load` jobs
    │── main_batch_processing.py  # operate the batch_processing module to do the `Transform` jobs
│── /tests                        # all small features unit testing snippets (DWH modelling, data pipeline, scheduler etc.) 
│── README.md                     # Introduction about project
│── docker-compose-bigdata.yml    # Docker Compose to launch the docker cluster
│── .env                          # `public the .env on purpose` for docker-compose file use
│── .gitignore                    # Git ignore some directory not to be committed to the remote repo
```

## 🚀 Quick Start `/src`

### [🔗 Source Code Instruction for Use](./src/README.md)
### 
### 

## 📌 Project Documents `/docs`

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
  - airflow 节点的搭建和配置 (airflow.cfg 里 mysql 和 localexecutor 的配置）
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

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.  
Created and maintained by **Smars-Bin-Hu**.
