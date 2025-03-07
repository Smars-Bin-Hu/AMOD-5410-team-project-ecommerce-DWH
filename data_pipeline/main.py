"""
main.py

Importing Modules
Layer1 : from project_directory import standard modules or third party modules
Layer2 : from project_directory.ext_mod import external modules in the project
Layer3 : import internal_modules ----- avoid circular importing
"""
from data_pipeline.configs import (
    LoggingConfig,
    DatabaseConnectionConfig,
    HadoopEnvConfig
)
from data_pipeline.utils import (
    LoggingUtils,
    OracleDatabaseUtils,
    HDFSUtils
)
from data_pipeline.core import (
    ETLOracleToHDFS,
    tables
)

# create a logger for current util
smars_dev_log_level = int(LoggingConfig.get_smars_dev_log_level())
smars_dev_log_level_name = LoggingConfig.get_smars_dev_log_level_name()
logger = LoggingUtils.setup_custom_logger(
    "ETL_MAIN_LOGGER",
    smars_dev_log_level,
    smars_dev_log_level_name
)

def main():
    logger.smars_dev("=== run ETL jobs ===")
    # 1. test Oracle connection
    # create oracle connection configuration instance
    oracle_db_config = DatabaseConnectionConfig("oracle","1")
    if not OracleDatabaseUtils.test_oracle_connection(oracle_db_config):
        logger.smars_dev("Terminal the job：Oracle failed to connect")
        return False

    # 2. check Hive ODS Layer HDFS target path
    hive_ods_hdfs_path = HadoopEnvConfig.get_hive_ods_hdfs_path()
    if not HDFSUtils.check_hdfs_path(hive_ods_hdfs_path):
        logger.smars_dev(f"HDFS path {hive_ods_hdfs_path} Not found")
        return False

    # 3. Run Spark Jobs (LOOP)
    # full load tables
    if len(tables) != 0:
        for table in tables:
            df = ETLOracleToHDFS.extract(table)
            if ETLOracleToHDFS.load(df, hive_ods_hdfs_path):
                logger.smars_dev(f"{table} loaded to HDFS")
            etl = ETLOracleToHDFS(table, oracle_db_config)
    else:
        logger.smars_dev(f"full_load_tables is empty")

    etl.run("MY_TABLE")  # 处理指定的 Oracle 表
    etl.stop()  # 关闭 SparkSession

    logging.info("=== ETL jobs finished ===")

if __name__ == "__main__":
    if main():
        logger.smars_dev(f"All ETL Jobs are finished")
