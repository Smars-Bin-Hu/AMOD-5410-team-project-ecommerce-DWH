"""
utils.py

Utils：including database connection and HDFS operations

"""

import cx_Oracle
import subprocess
import logging
import config

# set logging
logging.basicConfig(filename=config.LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class DatabaseUtils:
    """Oracle Database Utils"""

    @staticmethod
    def test_oracle_connection():
        """Test Whether the Oracle Connection is successful"""
        try:
            dsn = cx_Oracle.makedsn(config.ORACLE_HOST, config.ORACLE_PORT, sid=config.ORACLE_SID)
            conn = cx_Oracle.connect(user=config.ORACLE_USERNAME, password=config.ORACLE_PASSWORD, dsn=dsn)
            conn.close()
            logging.info("Oracle 数据库连接测试成功！")
            return True
        except Exception as e:
            logging.error(f"Oracle 数据库连接失败: {e}")
            return False

class HDFSUtils:
    """HDFS 相关操作"""

    @staticmethod
    def check_hdfs_path(hdfs_path):
        """检查 HDFS 路径是否存在"""
        try:
            cmd = f"hdfs dfs -ls {hdfs_path}"
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            logging.info(f"HDFS 目录存在: {hdfs_path}")
            return True
        except subprocess.CalledProcessError:
            logging.warning(f"HDFS 目录不存在: {hdfs_path}")
            return False

class LoggingUtils:
    """Logging Operations"""

    @staticmethod
    def setup_logger():
        """Setup the logger"""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.StreamHandler(),  # Terminal Stream Handler logging
            ],
        )
        return logging.getLogger("OracleToHDFS")