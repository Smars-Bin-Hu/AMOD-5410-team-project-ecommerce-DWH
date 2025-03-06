"""
utils.py

Utils：including database connection and HDFS operations

"""

import subprocess
import logging
import config as cfg
import jaydebeapi  # all NodeManager need install this API

# set logging
logging.basicConfig(filename=cfg.LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class OracleDatabaseUtils:
    """Oracle Database Utils"""

    @staticmethod
    def test_oracle_connection():
        """
        Test Whether the Oracle Connection is successful
        1) Load Oracle JDBC driver
        2) Connect to Oracle
        3) Execute a simple query, e.g. SELECT 1 FROM DUAL
        4) Return True if no exception, otherwise return False
        """
        try:
            logging.info("Attempting to connect to Oracle Database...")

            # JayDeBeApi need driver class, JDBC url, username&password list, and JDBC Driver path
            conn = jaydebeapi.connect(
                cfg.ORACLE_DRIVER,           # "oracle.jdbc.OracleDriver"
                cfg.ORACLE_JDBC_URL,         # "jdbc:oracle:thin:@//oracle-oltp:1521/ORCLPDB1"
                [cfg.ORACLE_USERNAME, cfg.ORACLE_PASSWORD],
                cfg.ORACLE_JDBC_DRIVER_PATH  # "/opt/spark/jars/ojdbc8.jar"
            )

            # if connect succeessfully, run a SQL
            with conn.cursor() as curs:
                curs.execute("SELECT 1 FROM DUAL")
                row = curs.fetchone()
                logging.info(f"Successfully retrieved row: {row}")
            conn.close()

            # No Exception, means Connected
            logging.info("Oracle Database Connected!")
            return True
        except Exception as e:
            logging.error(f"failed to connect Oracle Database: {e}")
            return False

class HDFSUtils:
    """HDFS Operations"""

    @staticmethod
    def check_hdfs_path(hdfs_path):
        """Check HDFS Path is existing"""
        try:
            # run HDFS command
            cmd = f"hdfs dfs -ls {hdfs_path}"
            subprocess.run(
                cmd,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            logging.info(f"HDFS is existing: {hdfs_path}")
            return True
        except subprocess.CalledProcessError:
            logging.warning(f"HDFS is non-existing: {hdfs_path}")
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