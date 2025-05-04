# /src/warehouse_modelling

## Project Structure

The codebase is organized as follows:

```text
/warehouse_modelling
├── ads_clickhouse/                # Application Data Service (ADS) layer for ClickHouse analytics
│   └── *.sql                      # DDL scripts defining final analytical tables (in ClickHouse)

├── dim/                           # Dimension layer
│   ├── hdfs/                      # HDFS initialization & SQL file upload scripts
│   └── *.sql                      # DDL for dimension tables

├── dwd/                           # Data Warehouse Detail layer (cleansed and detailed records)
│   ├── hdfs/                      # HDFS initialization & SQL file upload scripts
│   └── *.sql                      # DDL for dwd layers tables

├── dwm/                           # Data Warehouse Middle layer (detailed)
│   ├── hdfs/
│   └── *.sql

├── dws/                           # Data Warehouse Summary layer (aggregated by mid-level keys and summarized wide tables)
│   ├── hdfs/
│   └── *.sql

├── dwt/                           # Data Warehouse Topic layer (topic-wide tables, often for ads)
│   ├── hdfs/
│   └── *.sql

├── ods/                           # Operational Data Store layer (raw or lightly processed)
│   ├── avro_schema/              # Avro schemas for deserializing raw data
│   ├── hdfs/                     # HDFS initialization & raw DDL ingestion scripts
│   └── *.sql                     # DDL for ODS staging tables
```

Notes:
`*.sql` files in each directory define the schema (DDL) for that layer's tables.

The `hdfs/` folders contain initialization scripts or helpers to upload the corresponding SQL files to HDFS, typically for use in distributed execution.

The `avro_schema/` directory under `ods/` stores Avro schema definitions for raw data deserialization (e.g., during Kafka ingestion or batch loading).

The layered structure aligns with standard data warehouse design principles: from raw data capture (ODS), through detailed and intermediate transformations (DWD, DWM, DWS), to dimension modeling (DIM) and final presentation layers (DWT, ADS).