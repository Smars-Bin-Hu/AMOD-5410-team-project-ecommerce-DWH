# Tech Architecture

> [!NOTE]
> Back to the navigation map: [Document Navigation Map](../../README.md)

## Diagram 

![ECom-DWH-Pipeline](https://github.com/Smars-Bin-Hu/my-draw-io/blob/main/ECom-DWH-Datapipeline-Proejct/ECom-DWH-Tech-Arc.drawio.svg)

## Introduction

This technical architecture utilizes a three-node Hadoop distributed computing cluster deployed in Docker containers to provide highly reliable and scalable big-data storage and computation capabilities. The Hadoop cluster employs the HDFS for data storage and YARN for resource management and job scheduling. High availability (HA) of ResourceManagers and NameNodes is implemented using ZooKeeper coordination. The ResourceManagers run in an Active/Standby mode to support automatic failover and rapid fault recovery. Similarly, NameNodes ensure metadata consistency by synchronizing the edit logs through JournalNodes. The DFSZKFailoverController continuously monitors node statuses, enabling seamless node-switching and effectively eliminating single points of failure to guarantee stable business operations.

The Spark container serves as an independent client node. It hosts core services, including the Spark ThriftServer, which provides JDBC/ODBC interfaces. This allows external analytics or BI tools to connect using standard protocols. PySpark tasks submitted by users are first compiled by the Spark Driver within the Spark container. The Spark Driver initializes the SparkContext and uploads required JAR packages, Spark DAGs and dependencies onto HDFS. YARN's ApplicationMaster then distributes these tasks to Container Executors managed by NodeManagers within the cluster. Due to Spark's in-memory computation model, performance significantly surpasses traditional MapReduce, greatly reducing data processing times and making it particularly suitable for large-scale batch processing scenarios.

The Airflow container functions as an automated scheduling engine for batch data processing tasks. It automates daily data workflows through flexible DAGs. Airflow’s Scheduler manages Spark ETL job submissions, while its WebServer provides an interface for task monitoring, retries upon failures, and log management. The daily batch tasks scheduled by Airflow include incremental data extraction from Oracle databases into the Hive data warehouse. Subsequently, multi-layer data transformations occur within Hive, such as transitioning data from the ODS layer to DWD, or DWD to DIM, automating the management of partition refreshes and historical data backfilling. This significantly enhances data operations efficiency.

The Hive container primarily manages data warehouse modeling and metadata. It defines table schemas, partitions, and manages data metadata through HiveQL. Due to Hive’s reliance on MapReduce, which is slower compared to Spark, the design explicitly specifies that Hive does not typically handle analytical computation tasks. Instead, Hive's main function is metadata management and providing consistent metadata querying services for Spark.

Regarding system monitoring and operational management, the architecture includes a dedicated Monitoring container that hosts widely-adopted tools: Prometheus and Grafana. These tools provide real-time monitoring of cluster components, including Hadoop nodes and MySQL metadata databases, gathering performance metrics such as CPU usage, memory consumption, disk I/O, and network throughput. This monitoring solution provides visualizations and alerts, helping operational teams efficiently diagnose issues and optimize system performance.

MySQL serves as the centralized metadata store for Airflow and Hive. It does not store extensive business data directly but maintains critical metadata, including table definitions, partitioning information, and access permissions. This centralizes metadata maintenance, avoids redundancy, and ensures consistency between data management and job scheduling tasks.

Overall, this technical architecture is logically structured with clearly defined roles for containers and services. It achieves modularity, strong decoupling between services, efficient resource utilization, and simplified maintenance. Leveraging the advantages of containerized deployments, this solution meets enterprise-level requirements for high performance, high availability, and scalability, significantly improving the automation and stability of data processing workflows.

## Introduction (Mandarin)

本技术架构采用基于Docker容器化的三节点Hadoop分布式计算集群，以实现高可靠、高扩展的大数据存储与计算能力。Hadoop集群的分布式文件系统HDFS用于数据存储，YARN用于资源管理和作业调度。通过ZooKeeper实现ResourceManager和NameNode的双主高可用（HA）机制，ResourceManager以Active/Standby模式运行，实现自动容错和快速故障恢复，NameNode则通过JournalNode同步editlog日志以保障元数据一致性，DFSZKFailoverController进行节点状态监测和切换，有效防止单点故障，保障业务稳定运行。

Spark容器作为独立的客户端节点，安装了核心服务如Spark ThriftServer，能够支持JDBC/ODBC接口访问，通过标准化协议与外部分析工具或BI工具进行交互。用户提交的PySpark任务首先通过Spark容器的Driver进行任务编译和SparkContext初始化，将任务所依赖的Jar包、Spark DAG任务拓扑结构以及相关依赖包同步到HDFS，再经由YARN的ApplicationMaster将任务派发给集群中的NodeManager管理的Container Executor执行，从而高效地完成分布式计算任务。由于Spark基于内存计算，其计算性能远远高于传统MapReduce，大幅缩短数据任务执行时间，特别适合大规模批处理场景。

Airflow容器在本技术栈中作为批处理任务的自动化调度引擎，通过定义灵活的DAG任务流来实现每日定时数据任务的自动化执行。Airflow的调度器（Scheduler）负责提交Spark ETL任务，WebServer提供了任务监控、失败重试、日志查看的用户界面。Airflow每天调度的数据批处理任务包括从Oracle数据库增量抽取数据到Hive的数据仓库，然后在Hive内部进行多层数据模型转换，如ODS到DWD、DWD到DIM等分层数据加工，自动化管理数据分区刷新和历史数据回溯，大幅提高了数据运维效率。

Hive容器主要负责数据仓库的数据建模与元数据管理工作，通过HiveQL语言定义数据表schema、表分区管理和数据元信息维护。但Hive自身的分析和计算使用的MapReduce引擎性能较差，因此架构设计中明确指出Hive容器基本不用于实际的数据分析计算，其核心作用在于元数据管理及为Spark提供统一的元数据查询服务。

此外，监控与运维方面，本架构设置了单独的Monitoring容器，其中安装了业界主流的监控工具Prometheus和可视化监控平台Grafana，实时监测和收集集群内部各组件（如Hadoop节点、MySQL元数据库）的运行状态和性能指标，包括CPU、内存、磁盘I/O、网络吞吐量等，为运维团队提供直观的监控视图和告警功能，使系统的故障排查和优化更加高效。

作为统一的元数据中心，MySQL容器独立承担Airflow和Hive的数据仓库元数据（Metastore）的管理角色。MySQL不直接存储业务数据，而是集中存储表定义、分区信息、权限控制等关键元信息，实现了元数据的集中维护和高效管理，有效防止元数据的混乱和冗余，保证数据管理与任务调度之间的元数据一致性。

整体来看，本技术架构设计合理，各容器和服务角色清晰，模块化分工明确，服务解耦性强，高效利用资源并降低维护复杂性，体现了容器化部署的优势，满足了企业级大数据环境对高性能、高可用性和高扩展性的需求，极大地提升了业务数据处理的自动化和稳定性。