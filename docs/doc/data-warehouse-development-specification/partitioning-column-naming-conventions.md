# **Partitioning Column Naming Convention**

> [!NOTE]
> Back to the navigation map: [Document Navigation Map](../../../README.md)

- **`pt_`**: Generic partition column prefix
- **For Slowly Changing Dimensions (SCD Type 2, also known as "historical tracking tables"):**
    - **`pt_s`**: Start date of the record's validity period
    - **`pt_e`**: End date of the record's validity period

| **Partition Type** | **Partition Column** | **Partition Naming** | **Data Format** |
| --- | --- | --- | --- |
| **Hourly** | `pt_hour` | `yyyyMMddHH` | `2024022508` (Feb 25, 2024, 08:00) |
| **Daily** | `pt_date` | `yyyyMMdd` | `20240225` (Feb 25, 2024) |
| **Monthly** | `pt_month` | `yyyyMM` | `202402` (Feb 2024) |
| **Yearly** | `pt_year` | `yyyy` | `2024` |
| **Start Date (SCD)** | `pt_s` | `yyyyMMdd` | `20240101` (Jan 1, 2024 - Start Date) |
| **End Date (SCD)** | `pt_e` | `yyyyMMdd` | `20241231` (Dec 31, 2024 - End Date) |

### **Examples of Partitioned Table Definitions**

#### **Example 1: Hourly Partitioned Fact Table**

```sql
CREATE TABLE fact_order_transactions (
    order_id BIGINT,
    customer_id INT,
    order_amount DECIMAL(10,2),
    pt_hour CHAR(10) NOT NULL
) PARTITION BY RANGE (pt_hour) (
    PARTITION p_2024022508 VALUES LESS THAN ('2024022509'),
    PARTITION p_2024022509 VALUES LESS THAN ('2024022510')
);

```

#### **Example 2: Daily Partitioned Table**

```sql
CREATE TABLE dws_product_sales (
    product_id INT,
    total_sales DECIMAL(12,2),
    pt_date CHAR(8) NOT NULL
) PARTITION BY RANGE (pt_date) (
    PARTITION p_20240224 VALUES LESS THAN ('20240225'),
    PARTITION p_20240225 VALUES LESS THAN ('20240226')
);

```

#### **Example 3: Slowly Changing Dimension Table (SCD Type 2)**

```sql
CREATE TABLE dim_customer_history (
    customer_id INT,
    name VARCHAR(255),
    email VARCHAR(255),
    pt_s CHAR(8) NOT NULL,
    pt_e CHAR(8) NOT NULL
) PARTITION BY RANGE (pt_s) (
    PARTITION p_20230101 VALUES LESS THAN ('20240101'),
    PARTITION p_20240101 VALUES LESS THAN ('20250101')
);
```

### **Best Practices for Partitioning**

1. **Choose the appropriate partition type**:
    - **Hourly partitions** for real-time or streaming data
    - **Daily partitions** for most transaction-based systems
    - **Monthly/Yearly partitions** for long-term storage and analytics
    - **Start/End Date partitions** for **slowly changing dimensions (SCD Type 2)**
  
2. **Use partition pruning** to optimize query performance:
    - Ensure `WHERE pt_date = '20240225'` filters only the necessary partitions.
  
3. **Avoid excessive small partitions**:
    - If data volume is not large, prefer **daily over hourly** partitions.
  
4. **Automate partition management**:
    - Implement partition rotation, retention policies, and purging strategies.