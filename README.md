![1](https://github.com/user-attachments/assets/5b98ca67-3770-4d4a-b444-ad8b70c40557)

# Enterprise-Grade Offline Data Warehouse Solution for E-Commerce

<p align="center">
  <a href="https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/src/README/quick-start.md">
      <img src="https://img.shields.io/badge/project-🚀quick_start-blue?style=for-the-badge&logo=github" alt="Sublime's custom image"/>
  </a>
  <a href="https://github.com/Smars-Bin-Hu/EComDWH-Pipeline/tree/main/src">
      <img src="https://img.shields.io/badge/project-source_code-green?style=for-the-badge&logo=github" alt="Sublime's custom image"/>
  </a>
  <a href="https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/wiki">
      <img src="https://img.shields.io/badge/project-all%20documents-red?style=for-the-badge&logo=github" image"/>
   </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.12.9-blue?style=plastic&logo=python&logoColor=yellow&logoSize=auto&color=blue"/>
  <img src="https://img.shields.io/badge/apache_spark-3.3.0-blue?style=plastic&logo=apachespark&logoSize=auto&color=white"/>
  <img src="https://img.shields.io/badge/apache_hadoop-3.2.4-blue?style=plastic&logo=apachehadoop&logoColor=yellow&logoSize=auto&color=blue"/>
  <img src="https://img.shields.io/badge/apache_hive-3.1.3-blue?style=plastic&logo=apachehive&logoColor=yellow&logoSize=auto&color=yellow"/>
  <br>
  <img src="https://img.shields.io/badge/apache_zookeeper-3.8.4-79bb2e?style=plastic&color=79bb2e"/>
  <img src="https://img.shields.io/badge/mysql-8.0.39-blue?style=plastic&logo=mysql&logoColor=blue&logoSize=auto&color=blue"/>
  <img src="https://img.shields.io/badge/clickhouse-24.12-FFCC01?style=plastic&logo=clickhouse&logoColor=yellow&logoSize=auto&color=FFCC01"/>
  <img src="https://img.shields.io/badge/Prometheus-2.52.0-f2f2e8?style=plastic&logo=prometheus&logoColor=red&logoSize=auto&color=white"/>
  <img src="https://img.shields.io/badge/Grafana-10.3.1-f2f2e8?style=plastic&logo=Grafana&logoColor=red&logoSize=auto&color=white"/>
</p>

This project aims to build an enterprise-grade offline data warehouse solution based on e-commerce platform order data. By leveraging **Docker containers** to simulate a big data platform, it achieves a complete workflow from ETL processing to data warehouse modeling, OLAP analysis, and data visualization. 

The core value of this project lies in its implementation of **enterprise-grade data warehouse modeling**, integrating e-commerce order data with relevant business themes through standardized dimension modeling and fact table design, ensuring data accuracy, consistency, and traceability. Meanwhile, **the deployment of a big data cluster via Docker containers** simplifies environment management and operational costs, offering a flexible deployment model for distributed batch processing powered by Spark. Additionally, the project incorporates **CI/CD automation**, enabling rapid iterations while maintaining the stability and reliability of the data pipeline. Storage and computation are also **highly optimized** to maximize hardware resource utilization.

To monitor and manage the system effectively, a **Grafana-based cluster monitoring system** has been implemented, providing real-time insights into cluster health metrics and assisting in performance tuning and capacity planning. Finally, by integrating **business intelligence (BI) and visualization solutions**, the project transforms complex data warehouse analytics into intuitive dashboards and reports, allowing business teams to make data-driven decisions more efficiently.

By combining these critical features—including:

| ✅ Core Feature | 🔥 Core Highlights | 📦 Deliverables |
|-----------|------------------|---------------|
| **1. [Data Warehouse Modeling and Documentation](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main?tab=readme-ov-file#1-data-warehouse-modeling-and-documentation)** | - Full dimensional modeling process (Star Schema / Snowflake Schema) <br> - Standardized development norms (ODS/DWD/DWM/DWS/DWT/ADS six-layer modeling) <br> - Business Matrix: defining & managing dimensions & fact tables | - Data warehouse design document (Markdown) <br> - Hive SQL modeling code <br> - DWH Dimensional Modelling Architecture Diagram |
| **2. [A Self-Built Distributed Big Data Platform](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main?tab=readme-ov-file#2-a-self-built-distributed-big-data-platform)** | - Fully containerized deployment with Docker for quick replication <br> - High-availability environment: Hadoop + Hive + Spark + Zookeeper + ClickHouse | - Docker images (Open sourced on GitHub Container Registry) <br> - `docker-compose.yml` (one-click cluster startup) <br> - Infra Configuration Files for Cluster: Hadoop, ZooKeeper, Hive, MySql, Spark, Prometheus&Grafana, Airflow  <br> - Container Internal Scripts: Hadoop, ZooKeeper, Hive, MySql, Spark, Prometheus&Grafana, Airflow <br> - Common Used Snippets for Cluster: Hadoop, ZooKeeper, Hive, MySql, Spark, Prometheus&Grafana, Airflow |
| **3. [Distributed Batch Processing](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main?tab=readme-ov-file#3-distributed-batch-processing)** | - ETL processing using PySpark <br> - data ETL job: OLTP to DWH && DWH to OLAP  <br> - Data Warehouse internal processing: ODS → DWD → DIM/DWM → DWS → ADS <br> - batch processing job scheduler using Airflow | PySpark and Spark SQL Code <br> - Code - Data Pipeline (OLTP -> DWH, DWH -> OLAP) <br> - Code - Batch Processing (DWH Internal Transform) <br> - Code - Scheduling based on Airflow (DAGs) |
| **4. [CI/CD Automation](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main?tab=readme-ov-file#4-cicd-automation)** | - Automated data platform cluster launching and stop | - GitHub Actions workflow pipeline `.yaml` <br> - CI/CD code and documentation <br> - Sample log screenshots |
| **5. [Storage & Computation Optimization](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main?tab=readme-ov-file#5-storage--computation-optimization)** | - SQL optimization (dynamic partitioning, indexing, storage partitioning) <br> - Spark tuning: Salting, Skew Join Hint, Broadcast Join, `reduceByKey` vs. `groupByKey` <br> - Hive tuning: Z-Order sorting (boost ClickHouse queries), Parquet + Snappy compression | - Pre & post optimization performance comparison <br> - Spark optimization code <br> - SQL execution plan screenshots |
| **6. [DevOps - Monitoring and Alerting](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main?tab=readme-ov-file#6-devops---monitoring-and-alerting)** | - Prometheus + Grafana for performance monitoring Hadoop Cluster / MySQL <br> - AlertManager for alerting and email receiving | - Code - Monitoring Services Configuaration Files: Prometheus, Grafana, AlertManager <br> - Code - Monitoring Services Start&Stop Scripts: Prometheus, Grafana, AlertManager <br> - Code - Container Metrics Exporter Start&Stop Scripts: `my-start-node-exporter.sh` & `my-stop-node-exporter.sh` <br> - Key Screenshots |
| **7. [Business Intelligence & Visualization](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main?tab=readme-ov-file#7-business-intelligence--visualization)** | - PowerBI dashboards for data analysis <br> - Real business-driven visualizations <br> - Providing actionable business insights | - PowerBI visualization screenshots <br> - PowerBI `.pbix` file <br> - Key business metric explanations (BI Insights) |

this project delivers a professional, robust, and highly efficient solution for enterprises dealing with large-scale data processing and analytics.

## ⚙️ Core Deliverables

### 1. Data Warehouse Modeling and Documentation

This project demonstrates my ability to build a data warehouse from the ground up following enterprise-grade standards. I independently designed and documented a complete SOP for data warehouse development, covering every critical step in the modeling roadmap. From initial business data research to final model delivery, I established a standardized methodology that ensures clarity, scalability, and maintainability. The SOP includes detailed best practices on data warehouse layering, table naming conventions, field naming rules, and lifecycle management for warehouse tables. For more information, please refer to the documentation below.

<details>
  <summary>🔗 Click to Show DWH Dimensional Modelling Documents and Code</summary>
  
  - [DWH Modelling Standard Operation Procedure (SOP)](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/dwh-modelling-sop.md)
  - [Business Data Research](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/business_data_research.md)
  
  Data Warehouse Development Specification
  
  - [Data Warehouse Layering Specification](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/data-warehouse-development-specification/data-warehouse-layering-specification.md)
  - [Table Naming Conventions](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/data-warehouse-development-specification/table-naming-convertions.md)
  - [Data Warehouse Column Naming Conventions](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/data-warehouse-development-specification/partitioning-column-naming-conventions.md)
  - [Data Table Lifecycle Management Specification](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/data-warehouse-development-specification/data-table-lifecycle-management-specification.md)
  - [DWH Modelling Architecture Diagram](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/dwh-modelling-arch-diagram.md)


  [🔨 Code - Hive DDL](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main/src/warehouse_modeling)(for Data Warehouse All Layers including ods, dwd, dwm, dws, dwt, dim (Operational Data Storage, DW detail, DW middle, DW summary, DW theme, DW Dimension, Analytical Data Storage-CK)

</details>

![image](https://github.com/user-attachments/assets/ec924ea9-1acf-48a3-99ba-1546c1e8c3a9)
<p align="center"><em>Figure 1: DWH Dimensional Modelling SOP</em></p>

![image](https://github.com/user-attachments/assets/ab21c750-052f-4c10-baf0-bc97e5ed8274)
<p align="center"><em>Figure 2: DWH Dimensional Modelling Methodology Diagram</em></p>

![ECom-DWH-Pipeline](https://github.com/Smars-Bin-Hu/my-draw-io/blob/main/ECom-DWH-Datapipeline-Proejct/ECom-DWH-Pipeline.drawio.svg)
<p align="center"><em>Figure 3: DWH Dimensional Modelling Architecture</em></p>


### 2. A Self-Built Distributed Big Data Platform

This distributed data platform was built entirely from scratch by myself. Starting with a base Ubuntu 20.04 docker image, I manually installed and configured each component step by step, ultimately creating a fully functional three-node Hadoop cluster with distributed storage and computing capabilities. The platform is fully containerized, featuring a highly available HDFS and YARN architecture. It supports Hive for data warehousing, Spark for distributed computing, Airflow for workflow orchestration, and Prometheus + Grafana for performance monitoring. A MySQL container manages metadata for both Hive and Airflow and is also monitored by Prometheus. An Oracle container simulates the backend of a business system and serves as a data source for the data warehouse. All container images are open-sourced and published to [🔨 GitHub Container Registry](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/pkgs/container/proj1-dwh-cluster), making it easy for anyone to deploy the same platform locally.

[🔨 Code - Docker Compose File](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docker-compose-bigdata.yml)

[🔨 Code - Configuration Files for Cluster: Hadoop, ZooKeeper, Hive, MySql, Spark, Prometheus&Grafana, Airflow](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main/src/infra)

[🔨 Code - Container Internal Scripts: Hadoop, ZooKeeper, Hive, MySql, Spark, Prometheus&Grafana, Airflow](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main/src/scripts)

[🔨 Code - Common Used Snippets for Cluster: Hadoop, ZooKeeper, Hive, MySql, Spark, Prometheus&Grafana, Airflow](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main/src/snippets)

<img width="1500" alt="image" src="https://github.com/user-attachments/assets/576ce494-1d96-4b3c-992e-96addc1e6f43" />
<p align="center"><em>Figure 1: All Containers Window</em></p>

![ECom-DWH-Pipeline](https://github.com/Smars-Bin-Hu/my-draw-io/blob/main/ECom-DWH-Datapipeline-Proejct/ECom-DWH-Tech-Arc.drawio.svg)
<p align="center"><em>Figure 2: Data Platform Architecture</em></p>



### 3. Distributed Batch Processing

This project implements a robust distributed batch processing architecture using PySpark for computation and Apache Airflow for orchestration. The batch layer focuses on high-throughput, scalable ETL workflows and integrates seamlessly with the overall data warehouse design. The core functionalities are structured as follows:

1. [🔨 Code - Data Pipeline (OLTP -> DWH, DWH -> OLAP)](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main/src/data_pipeline)
   
A PySpark-based incremental extraction process is used to ingest new records from the Oracle OLTP database into the data warehouse. Additionally, downstream scripts handle the transformation and export of analytical and result-layer datasets from the data warehouse into external OLAP systems, enabling fast access by BI tools (e.g., Power BI, Tableau).

2.  [🔨 Code - Batch Processing (DWH Internal Transform)](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main/src/batch_processing)
   
Multi-stage transformations are implemented using Spark SQL within PySpark jobs to process data across warehouse layers, such as: ODS (Operational Data Store) → DWD (Data Warehouse Detail) and DWD → DIM (Dimension Tables). These transformations ensure structured, cleaned, and query-optimized data for analytical use cases.

3. [🔨 Code - Scheduling based on Airflow (DAGs)](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main/src/scheduler/dags)

The entire batch workflow is automated via Apache Airflow, with DAGs scheduled to run nightly at 2:00 AM. The scheduler coordinates the extraction, transformation, and loading tasks, handles dependencies, and ensures timely creation of new partitions and ingestion of the latest data into the warehouse.

![ECom-ETL-Data-Pipeline](https://github.com/Smars-Bin-Hu/my-draw-io/blob/main/ECom-DWH-Datapipeline-Proejct/ETL-data-pipeline-architecture.drawio.svg)
<p align="center"><em>Figure 1: ETL Data Pipeline</em></p>

<img width="2055" alt="image" src="https://github.com/user-attachments/assets/e74e33cd-8b9e-4913-8ce5-ad7a20793851" />
<p align="center"><em>Figure 2: Airflow Web UI</em></p>

### 4. CI/CD Automation

<a href="https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/actions/workflows/main.yml">
    <img src="https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/actions/workflows/main.yml/badge.svg" image"/>
</a>

1. GitHub Actions Code

[🔨 Code - workflows.main YAML](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/.github/workflows/main.yml)

2. Key Screenshots

<img width="1500" alt="image" src="https://github.com/user-attachments/assets/00fc170c-14ae-4f9d-a7e1-1480cb4d0112" />
<p align="center"><em>Figure 1: Data platform launching and stop automation</em></p>

<img width="1500" alt="image" src="https://github.com/user-attachments/assets/4a0a07fe-a629-4a10-a232-b01e0ed3aed2" />
<p align="center"><em>Figure 2: Sample Log Screenshot I </em></p>

<img width="1500" alt="image" src="https://github.com/user-attachments/assets/4c79ca68-286d-4f19-88a6-9917b565bc9e" />
<p align="center"><em>Figure 3: Sample Log Screenshot II </em></p>

3. [🔗 Link - Automation Workflow Web UI](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/actions)

### 5. Storage & Computation Optimization

### 6. DevOps - Monitoring and Alerting

[🔨 Code - Monitoring Services Configuaration Files: Prometheus, Grafana, AlertManager](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main/src/infra/monitoring-config)

[🔨 Code - Monitoring Services Start&Stop Scripts: Prometheus, Grafana, AlertManager](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main/src/scripts/monitoring)

[🔨 Code - Container Metrics Exporter Start&Stop Scripts: `my-start-node-exporter.sh` & `my-stop-node-exporter.sh`](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/tree/main/src/scripts/hadoop-master)

<img width="1500" alt="Prometheus" src="https://github.com/user-attachments/assets/2f157fd1-1e41-4090-9c74-0fc3e97e385e" />
<p align="center"><em>Figure 1: Prometheus</em></p>
<img width="1501" alt="Grafana-Hadoop-Cluster-instance-hadoop-master" src="https://github.com/user-attachments/assets/7c4d94ca-3262-46be-adb3-18c3777a314f" />
<p align="center"><em>Figure 2: Grafana-Hadoop-Cluster-instance-hadoop-master</em></p>
<img width="1495" alt="Grafana-MySQLD" src="https://github.com/user-attachments/assets/7df991be-3642-4ad4-9672-3d8483423178" />
<p align="center"><em>Figure 3: Grafana-MySQLD</em></p>

### 7. Business Intelligence & Visualization

[🔗 Link - PowerBI Public Access(Expirable)](https://app.powerbi.com/view?r=eyJrIjoiMzVjYTQ3NmMtODllZS00N2JhLWFkNWItMWI4MmYyNDZjMDc1IiwidCI6IjI0MGI3OWM1LTZiZWYtNDYwOC1hNDE3LTY1NjllODQzNTQ1YyJ9)

Use Microsoft PowerBI connect to the Clickhouse and extract the **analytical data storage** layer
<img width="1500" alt="image" src="https://github.com/user-attachments/assets/21eaea88-0fac-488d-9696-3be5720b4ac3" />
<p align="center"><em>Figure 1: PowerBI Dashboard Demo</em></p>

## Tech Stack

This project sets up a high-availability big data platform, including the following components:

![Apache Spark](https://img.shields.io/badge/Spark-FDEE21?style=for-the-badge&logo=apachespark&logoColor=black) 	![Apache Hadoop](https://img.shields.io/badge/Hadoop-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=black) ![Apache ZooKeeper](https://img.shields.io/badge/Zookeeper-8e8c3a?style=for-the-badge&color=8e8c3a) ![Apache Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white) ![Apache Hive](https://img.shields.io/badge/Hive-FDEE21?style=for-the-badge&logo=apachehive&logoColor=black)  ![ClickHouse](https://img.shields.io/badge/ClickHouse-FFCC01?style=for-the-badge&logo=clickhouse&logoColor=white) ![Prometheus](https://img.shields.io/badge/Prometheus-f2f2e8?style=for-the-badge&logo=prometheus&color=f2f2e8) ![Grafana](https://img.shields.io/badge/Grafana-252523?style=for-the-badge&logo=grafana&color=252523)  ![MySQL](https://img.shields.io/badge/MySQL-blue?style=for-the-badge&logo=mysql&logoColor=yellow&color=blue) ![Oracle Database](https://img.shields.io/badge/Oracle_Database-red?style=for-the-badge&color=red) ![Microsoft PowerBI](https://img.shields.io/badge/Microsoft_PowerBI-pink?style=for-the-badge&color=pink) 
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) 

| Components             | Features                       | Version |
|------------------------|--------------------------------|---------|
| Apache Hadoop          | Big Data Distributed Framework | 3.2.4   |
| Apache Zookeeper       | High Availability              | 3.8.4   |
| Apache Spark           | Distributed Computing          | 3.3.0   |
| Apache Hive            | Data Warehousing               | 3.1.3   |
| Apache Airflow         | Workflow Scheduling            | 2.7.2   |
| MySQL                  | Metastore                      | 8.0.39  |
| Oracle Database        | Workflow Scheduling            | 19.0.0  |
| Azure Cloud ClickHouse | OLAP Analysis                  | 24.12   |
| Microsoft PowerBI      | BI Dashboard                   | latest  |
| Prometheus             | Monitoring                     | 2.52.0  |
| Grafana                | Monitoring GUI                 | 10.3.1  |
| Docker                 | Containerization               | 28.0.1  |

## 📁 Project Directory

```bash
/bigdata-datawarehouse-project
│── /.github/workflows            # CI/CD automation workflows via GitHub Actions
│── /docs                         # docs (all business and technologies documents about this project)
│── /src
    │── /data_pipeline            # ETL flow: OLTP2DWH & DWH2OLAP
    │── /warehouse_modeling       # DWH modelling（Hive SQL etc.）
    │── /batch_processing         # Data Batch processing (PySpark + SparkSQL)
    │── /scheduler                # Task Scheduler(Airflow DAGs)
    │── /infra                    # infrastructure deployment(Docker, configuration files)
    │── /snippets                 # common used commands and snippets
    │── /scripts                  # container internal shell scripts
    │── /bi                       # PowerBI Dashboard pbix file
    │── /README                   # Source Code Use Instruction Markdown Files
    │── README.md                 # Navigation of Source Code Use Instruction
    │── main_data_pipeline.py     # **main entry point for the data pipeline module
    │── main_batch_processing.py  # **main entry point for the batch processing module
│── /tests                        # all small features unit testing snippets (DWH modelling, data pipeline, dags etc.) 
│── README.md                     # Introduction about project
│── docker-compose-bigdata.yml    # Docker Compose to launch the docker cluster
│── .env                          # `public the .env on purpose` for docker-compose file use
│── .gitignore                    # Git ignore some directory not to be committed to the remote repo
│── .gitattributes                # Git repository attributes config
│── LICENSE                       # COPYRIGHT for this project
│── mysql-metadata-restore.sh     # container operational level scripts: restore mysql container metadata
│── mysql-metastore-dump.sh       # container operational level scripts: dump mysql container metadata
│── push-to-ghcr.sh               # container operational level scripts: push the images to GitHub Container Registry
│── start-data-clients.sh         # container operational level scripts: start hive, spark etc
│── start-hadoop-cluster.sh       # container operational level scripts: start hadoop HA cluster 
│── start-other-services.sh       # container operational level scripts: start airflow, prometheus, grafana etc
│── stop-data-clients.sh          # container operational level scripts: stop hive, spark etc
│── stop-hadoop-cluster.sh        # container operational level scripts: stop hadoop HA cluster 
│── stop-other-services.sh        # container operational level scripts: stop airflow, prometheus, grafana etc
```

## 🚀 [Source Code Instruction for Use](./src/README.md) `/src`

### [🚀 Cluster Quick Start](./src/README/quick-start.md)

### Data Pipeline Instruction

#### [🚀 /src/data_pipeline + /src/main_data_pipeline.py](./src/README/spark-upstream.md)
#### [🚀 /src/data_pipeline + /src/main_data_pipeline.py](./src/README/spark-downstream.md)

### Batch Processing Instruction

#### [🚀 /src/batch_processing + /src/main_batch_processing.py](./src/README/batch_processing.md)

### Warehouse Modelling Instruction

#### [🚀 /src/warehouse_modelling](./src/README/warehouse_modelling.md)

### Automation Scheduler Instruction

#### [🚀 /src/scheduler](./src/README/scheduler.md)

### Container DevOps Scripts Instruction

#### [🚀 /src/scripts](./src/README/scripts.md)


## 📌 Project Documents `/docs`

#### 1. Tech Architecture

- [Project Tech Architecture](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/tech-architecture.md)

#### 2. Development Specification

- Data Warehouse Development Specification
  - [Business Data Research](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/business_data_research.md)
  - [DWH Modelling Standard Operation Procedure (SOP)](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/dwh-modelling-sop.md)
  - [Data Warehouse Layering Specification](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/data-warehouse-development-specification/data-warehouse-layering-specification.md)
  - [Table Naming Conventions](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/data-warehouse-development-specification/table-naming-convertions.md)
  - [Data Warehouse Column Naming Conventions](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/data-warehouse-development-specification/partitioning-column-naming-conventions.md)
  - [Data Table Lifecycle Management Specification](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/data-warehouse-development-specification/data-table-lifecycle-management-specification.md)
  - [DWH Modelling Architecture Diagram](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/dwh-modelling-arch-diagram.md)

- SQL Development Specification
  - [Development Specification](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/data-warehouse-development-specification/development-specification.md)

#### 3. Troubleshooting

  - [Troubleshooting: NodeManager Disk Space Issue Preventing YARN Registration](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/04_MAR_2025.md)
  - [Troubleshooting: Spark on Yarn submit encounter Container exited with a non-zero exit code 13. Error file: prelaunch.err.](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/05_MAR_2025.md)
  - [Troubleshooting: Error Handling Log: YARN Web UI Log Loading Failures](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/06_MAR_2025.md)
  - [Troubleshooting: Docker Container Running Out of Memory](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/06_MAR_2025_02.md)
  - [Troubleshooting: Spark Task - Issue with Writing ODS Layer Avro Data to HDFS but Hive Cannot Read](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/07_MAR_2025.md)
  - [Troubleshooting: JSON-like Dictionary Representation in Python Script Causes Execution Failure](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/08_MAR_2025.md)
  - [Troubleshooting: Partitioned table NO DATA displayed while hive SQL query, even though data file existing on HDFS](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/10-MAR-2025_02.md)
  - [Troubleshooting: Resolving "Unrecognized column type: DATE_TYPE" Issue on ods_orders_ipd Table](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/10-MAR-2025.md)
  - [Troubleshooting Hive Unable to Read Parquet Files Written by Spark SQL](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/13-MAR-2025.md)
  - [Troubleshooting: java.lang.NoClassDefFoundError: org/apache/hc/client5/http/io/HttpClientConnectionManager](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/17-MAR-2025.md)
  - [Troubleshooting NameNode Startup Failure in Hadoop HA Environment](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/21-MAR-2025.md)
  - [Preventing SIGHUP from Killing Background Processes When Using Docker `exec -it`](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/22-MAR-2025-2.md)
  - [Troubleshooting Document: Git Line Ending Conversion Issue Causing JournalNode/NameNode Startup Failure](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/22-MAR-2025.md)

  - [Bugs Need To Be Fixed in Future](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/error-handling/future-fix.md)

#### Development 

#### Testing 

#### Optimization

  - [Too many INFO logs: Reducing Spark Console Log Levels](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform/blob/main/docs/doc/optimization/reducing-spark-console-log-levels.md)

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.  
Created and maintained by **Smars-Bin-Hu**.
