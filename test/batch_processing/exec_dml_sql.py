from pyspark.sql import SparkSession

def main():
    spark = (
        SparkSession.builder
        .appName("UT - ods_to_Dwd")
        .enableHiveSupport()  # 一般也需要启用 Hive 支持
        .config("spark.sql.parquet.writeLegacyFormat", "true")
        # 如果还有时间/日期字段不兼容，也可能需要 .config("spark.sql.parquet.int96AsTimestamp", "true")
        .getOrCreate()
    )

    # from current folder
    sql = \
    """
        INSERT OVERWRITE TABLE dwd.dwd_campaign_product_subcategory_fpd
        SELECT
            campaign_product_subcategory_id,
            campaign_id,
            subcategory_id,
            discount
        FROM
            ods.ods_campaign_product_subcategory_fpd;
    """

    spark.sql(sql)

    spark.stop()

if __name__ == '__main__':
    main()