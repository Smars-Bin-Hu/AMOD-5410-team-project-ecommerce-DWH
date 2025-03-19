from pyspark.sql.functions import col, to_date
from data_pipeline.configs import (
    DatabaseConnectionConfig,
    hive2ck_tables_configs
)
from data_pipeline.utils import logger
from .load_ck import load_to_ck

# record the result of hive and ck tables
successful_access_hive_tables = []
empty_hive_tables = []
failed_access_hive_tables = []
successful_load_ck_tables = []
failed_access_ck_tables = []

# Connect the CK, Loading Clickhouse Connection Config
ck_db_config = DatabaseConnectionConfig("clickhouse","1")
ck_properties = ck_db_config.get_properties("clickhouse","1")
ck_host = ck_properties["host"]
ck_port = ck_properties["port"]
ck_user = ck_properties["user"]
ck_password = ck_properties["password"]

def spark_load_hive_to_ck(spark) -> bool:
    # config Spark Job
    spark.conf.set("spark.sql.catalog.clickhouse", "com.clickhouse.spark.ClickHouseCatalog")
    spark.conf.set("spark.sql.catalog.clickhouse.protocol", "https")
    spark.conf.set("spark.sql.catalog.clickhouse.host", ck_host)
    spark.conf.set("spark.sql.catalog.clickhouse.http_port", ck_port)
    spark.conf.set("spark.sql.catalog.clickhouse.user", ck_user)
    spark.conf.set("spark.sql.catalog.clickhouse.password", ck_password)
    spark.conf.set("spark.sql.catalog.clickhouse.option.ssl", "true")
    spark.conf.set("spark.clickhouse.write.format", "json")

    for table in hive2ck_tables_configs:
        # Loading clickhouse table info
        hive_db = table["hive_db"]
        hive_tbl = table["hive_table"]
        hive_tbl_partition_field = table["hive_table_partition_field"]
        partition_data = table["load_data_partition_data"]
        ck_db = table["ck_db"]
        ck_tbl = table["ck_table"]

        logger.smars_dev(f"Starting load hive table: {hive_db}.{hive_tbl} to clickhouse:{ck_db}.{ck_tbl}" )
        try:
            # Step 1: Read Hive Data
            # generate spark sql
            if hive_tbl_partition_field == "data_date":
                sql = f"SELECT * FROM {hive_db}.{hive_tbl} WHERE {hive_tbl_partition_field} = '{partition_data}';"
            elif hive_tbl_partition_field is None:
                sql = f"SELECT * FROM {hive_db}.{hive_tbl};"
            logger.smars_dev(f"DEBUG: Spark SQL: {sql}")

            # read data from hive
            df = spark.sql(sql)
            df.show() # debug

            # data date partition field casting from String to Date (otherwise it cannot be parse by ck and would be 1970-01-01)
            if hive_tbl_partition_field == "data_date":
                df = df.withColumn("data_date", to_date(col("data_date")))  # make sure this is DateType

            if df.schema is None: # Case 3: Extraction failed
                failed_access_hive_tables.append(hive_db+"."+hive_tbl)
                continue # skip the load clickhouse step

            if df.isEmpty():  # Case 2: Table exists, but has no data
                empty_hive_tables.append(hive_db+"."+hive_tbl)
                continue # skip the load clickhouse step

            successful_access_hive_tables.append(hive_db+"."+hive_tbl)

            # Step 2: Load data to Clickhouse
            spark.conf.set("spark.sql.catalog.clickhouse.database", ck_db)
            success = load_to_ck(ck_db, ck_tbl, df)

            if success:
                successful_load_ck_tables.append(ck_db+"."+ck_tbl)
                logger.smars_dev(f"Successfully loaded table: {ck_tbl}")
            else:
                failed_access_ck_tables.append(ck_tbl)
                logger.smars_dev(f"Failed to load table: {ck_tbl}")
        except Exception as e:
            logger.smars_dev(f"Error processing table {ck_tbl}: {e}")

    logger.smars_dev("=== Load Hive to CK jobs finished ===")
    logger.smars_dev(f"Successfully Extracted: {successful_access_hive_tables}")
    logger.smars_dev(f"Failed to access hive tables: {failed_access_hive_tables}")
    logger.smars_dev(f"Empty tables on Hive: {empty_hive_tables}")
    logger.smars_dev(f"Successfully Loaded CK: {successful_load_ck_tables}")
    logger.smars_dev(f"Failed to Load CK: {failed_access_ck_tables}")
    return True