# **Table Naming Conventions**

> [!NOTE]
> Back to the navigation map: [Document Navigation Map](../../../README.md)

Tables in the data warehouse should follow a structured naming convention to ensure clarity, consistency, and maintainability. The format is:

### **Naming Format**

```
Layer + Subject + Table Name + [Processing Method + Retention Period + Update Frequency] / (_manual)

```

- `_manual` suffix: Indicates a **static table** that does not undergo periodic updates and is manually maintained.

### **Components Explanation**

#### **Processing Method**

- **i**: Full data load
- **f**: Incremental data load
- **z**: Slowly changing dimension (SCD, type 2 history tracking)

#### **Retention Period**

- **p**: Permanent storage
- **{x}m**: Retains data for **x months, like 3m, 6m,etc**
- **{x}y**: Retains data for **x years, like 1y, 2y,etc**

#### **Update Frequency**

- **r**: Real-time updates
- **h**: Hourly updates
- **d**: Daily updates
- **w**: Weekly updates
- **m**: Monthly updates
- **q**: Quarterly updates
- **y**: Yearly updates

#### **Interpretation of Naming Convention**

The suffix `[Processing Method + Retention Period + Update Frequency]` describes the periodicity of data processing and retention. Examples:

- **ipd**: Incremental load, permanently stored, updated daily
- **fpd**: Full load, permanently stored, updated daily
- **i3md**: Incremental load, retains data for **3 months**, updated daily

#### **Example Table Names**

- `dws_product_item_details_ipd` → **Data Warehouse Service (DWS) layer**, product item details, incremental load, permanent storage, daily updates.
- `dim_customer_fpd` → **Dimension (DIM) table**, customer data, full load, permanent storage, daily updates.

This naming standard ensures clarity in data storage, processing methodology, and update schedules within the data warehouse. It facilitates efficient ETL processing, data governance, and long-term maintenance.
