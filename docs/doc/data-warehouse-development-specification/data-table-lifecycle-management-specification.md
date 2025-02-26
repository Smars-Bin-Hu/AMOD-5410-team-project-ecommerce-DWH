# **Data Table Lifecycle Management Specification**


> [!NOTE]
> Back to the navigation map: [Document Navigation Map](../../../README.md)

### **1. Classification of Data Importance (P0, P1, P2, P3)**

To ensure efficient storage, retrieval, and archival of data, tables in the data warehouse are classified into four priority levels:

| **Priority Level**          | **Definition**                                                                                                                                 | **Recoverability**  | **Example**                                                     |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------- |
| **P0** (Critical Data)      | Highly important domain data and critical application data. Data loss is**irreversible** and can cause **severe business impact**.       | **Not Recoverable** | Core business transactions, financial ledger, customer account data.  |
| **P1** (Important Data)     | Important business and application data. Loss of this data is**not recoverable** but has **slightly lower impact** compared to P0.       | **Not Recoverable** | Historical transaction logs, key analytical reports, compliance logs. |
| **P2** (Intermediate Data)  | Important business and application data, but**can be recovered** through reprocessing. Typically includes ETL-generated intermediate datasets. | **Recoverable**     | ETL transformation logs, temporary aggregation tables.                |
| **P3** (Non-Essential Data) | Non-critical business and application data, which is**fully recoverable** from source systems or recomputation.                                | **Recoverable**     | Caching tables, temporary reports, non-essential logs.                |

### **2. Data Retention Policy by Layer**

The retention policy varies by the data warehouse layer and priority level.

#### **2.1 ODS / DWD (Raw and Cleansed Data Layer)**

| **Table Type**                         | **P0** | **P1** | **P2** | **P3** |
| -------------------------------------------- | ------------ | ------------ | ------------ | ------------ |
| **Event Stream Table (Incremental)**   | Permanent    | 5 years      | 3 years      | 1 year       |
| **Event Snapshot Table (Incremental)** | Permanent    | 5 years      | 3 years      | 1 year       |
| **Dimension Table (Full)**             | 3 years      | 2 years      | 365 days     | 33 days      |
| **Merged Full Table**                  | 2 years      | 2 days       | 2 days       | 2 days       |
| **General Full Table**                 | 3 years      | 365 days     | 365 days     | 180 days     |
| **New Synchronization Full Table**     | 3 years      | 3 days       | 3 days       | 3 days       |

#### **2.2 DWM + DIM (Detailed and Dimension Layer)**

| **Table Type**                          | **P0**  | **P1**  | **P2**  | **P3**  |
| --------------------------------------------- | ------------- | ------------- | ------------- | ------------- |
| **Event Stream Table (Incremental)**    | Permanent     | 5 years       | 3 years       | 1 year        |
| **Event Snapshot Table (Incremental)**  | Permanent     | 5 years       | 3 years       | 1 year        |
| **Dimension Table (Full + SCD Type 2)** | 33 days + SCD | 33 days + SCD | 33 days + SCD | 33 days + SCD |
| **General Full Table**                  | 3 years       | 365 days      | 365 days      | 180 days      |

#### **2.3 DWS + DWT (Aggregated and Analytical Layer)**

| **Table Type**         | **P0** | **P1** | **P2** | **P3** |
| ---------------------------- | ------------ | ------------ | ------------ | ------------ |
| **Granular Fact Data** | Permanent    | 3 years      | 3 years      | 3 years      |

#### **2.4 Temporary Storage Layer**

| **Table Type**             | **P0** | **P1** | **P2** | **P3** |
| -------------------------------- | ------------ | ------------ | ------------ | ------------ |
| **ETL Temporary Table**    | 7 days       | 3 days       | 3 days       | 3 days       |
| **Other Temporary Tables** | 7 days       | 7 days       | 7 days       | 7 days       |

#### **2.5 ADS (Application Data Layer)**

| **Table Type**          | **P0** | **P1** | **P2** | **P3** |
| ----------------------------- | ------------ | ------------ | ------------ | ------------ |
| **Operational Reports** | Permanent    | --           | --           | --           |
| **External Data**       | 7 years      | --           | --           | --           |
| **Internal Products**   | 3 years      | --           | --           | --           |
