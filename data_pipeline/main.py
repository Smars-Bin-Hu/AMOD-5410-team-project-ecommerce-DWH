"""
main.py

Programme Entrance
1. connect the Oracle
2. testing the connection
2. run Sqoop jobs
"""

import logging
import config
from utils import DatabaseUtils, HDFSUtils
from oracle_to_hdfs import OracleToHDFS

def main():
    logging.info("=== run ETL jobs ===")

    # 1. test Oracle connection
    if not DatabaseUtils.test_oracle_connection():
        logging.error("Terminal the job：Oracle failed to connect")
        return

    # 2. check HDFS target path
    if not HDFSUtils.check_hdfs_path(config.HDFS_PATH):
        logging.warning(f"HDFS path {config.HDFS_PATH} Not found，Sqoop will create automatically")

    # 3. Run Spark Jobs
    etl = OracleToHDFS()  # connect ETL instance
    etl.run("MY_TABLE")  # 处理指定的 Oracle 表
    etl.stop()  # 关闭 SparkSession

    logging.info("=== ETL jobs finished ===")

if __name__ == "__main__":
    main()
