from pyspark.sql import SparkSession
import re
from datetime import datetime
from typing import Union

# Jobs - ods_to_dwd
def main():
    spark = (
        SparkSession.builder
        .appName("UT - ods2dwd")
        .enableHiveSupport()  # 一般也需要启用 Hive 支持
        .config("spark.sql.parquet.writeLegacyFormat", "true")
        # 如果还有时间/日期字段不兼容，也可能需要 .config("spark.sql.parquet.int96AsTimestamp", "true")
        .getOrCreate()
    )

    sql_path = sql_dml_files_path_dwd.get("dml_dwd_campaign_product_subcategory_fpd")

    try:
        raw_sql = read_sql(sql_path)
        sql = sql_render_partition_date(raw_sql, "2025-")
        spark.sql(sql)   # execute sql
    except Exception as e:
        None

    spark.stop()

# Configs - sql file path
sql_dml_files_path_dwd = \
    {
        "dml_dwd_campaign_product_subcategory_fpd" : "./dml_sql/dml_dwd_customer_product_ratings_ipd.sql",
    }

# Utils - read_sql
def read_sql(file_path : str):
    with open(file_path, 'r', encoding='utf-8') as file:
        sql = file.read()
    return sql

DATE_PATTERN = r"\d{4}-\d{2}-\d{2}"  # 格式校验正则

# Utils - sql render partition date
def sql_render_partition_date(
    raw_sql: str,
    data_date: Union[str, datetime],
    placeholder: str = "${data_date}"
)-> str:
    if isinstance(data_date, datetime):
        date_str = data_date.strftime("%Y-%m-%d")
    else:
        date_str = data_date

    if not re.fullmatch(DATE_PATTERN, date_str):
        raise ValueError(f"Invalid date format: {date_str}, expected YYYY-MM-DD")

    sql = raw_sql.replace(placeholder, date_str)

    return sql

if __name__ == '__main__':
    main()