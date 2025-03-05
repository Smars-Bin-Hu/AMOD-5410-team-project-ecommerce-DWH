"""
oracle_to_hdfs.py

This Module: define OracleToHDFS class, to extract the data from Oracle and load to the HDFS
"""

from pyspark.sql import SparkSession
from config import Config # Config.py

# Utils.py
from utils import LoggingUtils
from utils import DatabaseUtils
from utils import HDFSUtils

class OracleToHDFS:
    """Oracle 数据拉取并存储至 HDFS 的 ETL 任务类"""

    def __init__(self):
        """
            Constructor:
                initialize SparkSession and Logging System
         """

        # launch the Logging System
        self.logger = LoggingUtils.setup_logger()
        self.logger.info("Initializing SparkSession...")

        # launch the SparkSession
        self.spark = SparkSession.builder \
            .appName(Config.SPARK_APP_NAME) \
            .config("spark.driver.extraClassPath", Config.SPARK_JDBC_DRIVER_PATH) \
            .getOrCreate()

    def extract(self, table_name):
        """extract 1 table from Oracle"""
        self.logger.info(f"Read Oracle Table: {table_name}")

        # config the user information
        properties = {
            "user": Config.ORACLE_USER,
            "password": Config.ORACLE_PASSWORD,
            "driver": Config.ORACLE_DRIVER
        }

        # connect Oracle using Service Name instead of SID
        ORACLE_JDBC_URL = f"jdbc:oracle:thin:@//{Config.ORACLE_HOST}:{Config.ORACLE_PORT}/{Config.ORACLE_SERVICE_NAME}"

        # get the table
        df = self.spark.read.jdbc(url=ORACLE_JDBC_URL, table=table_name, properties=properties)

        return df

    def transform(self, df):
        """（可选）数据转换逻辑"""
        self.logger.info("数据转换：当前无特殊转换逻辑")
        return df  # 目前不做转换，直接返回原始数据

    def load(self, df):
        """写入数据到 HDFS"""
        self.logger.info(f"数据写入 HDFS: {Config.HDFS_PATH}")
        df.write.mode("overwrite").parquet(Config.HDFS_PATH)

    def run(self, table_name):
        """执行完整的 ETL 流程"""
        self.logger.info(f"开始处理表: {table_name}")

        # 1. 抽取数据
        df = self.extract(table_name)

        # 2. 进行转换（这里暂时不做转换）
        df_transformed = self.transform(df)

        # 3. 加载到 HDFS
        self.load(df_transformed)

        self.logger.info("ETL 任务完成！")

    def stop(self):
        """停止 SparkSession"""
        self.logger.info("正在关闭 SparkSession...")
        self.spark.stop()
