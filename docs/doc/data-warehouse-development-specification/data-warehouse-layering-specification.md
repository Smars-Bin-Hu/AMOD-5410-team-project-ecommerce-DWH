
# Data Warehouse Layering Specification

> [!NOTE]
> Back to the navigation map: [Document Navigation Map](../../../README.md)

### Data Warehouse Layering

|  | Layer | Summary | Definition | Purpose |
| --- | --- | --- | --- | --- |
| ODS Layer (Operational Data Store) | ODS | Original Data (Dirty) | The **ODS (Operational Data Store) layer** stores raw data from source systems **without modifications**.| It serves as the foundation for all downstream transformations and aggregations. <br> Act as a **backup of the original data** before any transformation. <br> Provide a **single version of truth** from all source systems. |
| DW Layer (Enterprise Data Warehouse) | DWD | Clean, Masking and standard original data, finest granularity | The **DWD (Detail Layer)** is the first transformation layer after ODS. |  It ensures data quality and standardization after data cleaning, data standardization, data masking etc. <br>  Preparation area between real DWH and original data. |
| DW Layer (Enterprise Data Warehouse) | DWM | detailed fact tale, finest granularity | The **DWM (Middle Layer)** keeps the fact table details, the same **granularity as DWD,** and expand the dimension in the model (snow schema) | Prepare for data aggregating.  |
| DW Layer (Enterprise Data Warehouse) | DWS | lightly aggregated fact table | The **DWS (Summary Layer)** slightly aggregates middle layer **data** into a wide-table. | Reduce data volume by pre-aggregating common metrics.  <br>  Improve query speed for business reporting. |
| DW Layer (Enterprise Data Warehouse) | DWT | highly aggregated fact table with accumulated summary data | The **DWT (Theme Layer)** structures data into **analytical themes** based on business indicators.| Keeps the accumulated summary data like some summary metric in past 7 days, past 30 days, and past 3 months, etc. <br>  Create **business-focused, pre-calculated metrics tables**. <br>  Enable **time-series calculations** (first-time, last-time, cumulative calculations). <br>  Support BI tools with **fast, pre-aggregated metrics**. |
| DW Layer (Enterprise Data Warehouse) | DIM | dimension table | **Dimension tables** store descriptive attributes related to business entities (e.g., customers, products, stores). | Provides contextual details for fact tables.  <br> Supports hierarchical relationships (e.g., country → region → city). <br>  Facilitates drill-down analysis in BI reports. |
| ADS Layer(Application Data Service) | ADS | For application data | The **ADS (Application Data Service) layer** provides **final processed data** for BI dashboards, real-time analytics, and reporting tools. | For Data analytics, generating reports, BI dashboard, Machine Learning, API data service development. |

### Compression & Storage Format Choice

- Avro for ODS
- PARQUET for spark, ORC for Hive

| Layer | Compression Format | Storage **Format** | Reason of CF |
| --- | --- | --- | --- |
| ODS | Gzip | AVRO | Efficient row-based storage| schema evolution support |
| DWD | Snappy | PARQUET | For Spark computation.  <br>  Optimized for analytical workloads, best for aggregations.  <br>  Fast query performance, high compression. |
| DWM | Snappy | PARQUET | For Spark computation.  <br>  Optimized for analytical workloads, best for aggregations.  <br>  Fast query performance, high compression. |
| DWS | Snappy | PARQUET | For Spark computation.  <br>  Optimized for analytical workloads, best for aggregations.  <br>  Fast query performance, high compression. |
| DWT | Snappy | PARQUET | For Spark computation.  <br>  Optimized for analytical workloads, best for aggregations.  <br>  Fast query performance, high compression. |
| DIM | Snappy | PARQUET | Optimized for fast joins with fact tables. |

