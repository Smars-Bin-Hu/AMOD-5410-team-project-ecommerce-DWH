"""
utils.py

Utils：including database connection and HDFS operations

"""

import subprocess
import logging
from config import Config
import jaydebeapi  # all NodeManager need install this API

# set logging
logging.basicConfig(
    filename=Config.LoggingConfig.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


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
            logging.info("Smars Debug======>>>>>>>: Attempting to connect to Oracle Database...")

            # JayDeBeApi need driver class, JDBC url, username&password list, and JDBC Driver path
            conn = jaydebeapi.connect(
                Config.OracleDBConfig.ORACLE_DRIVER,  # "oracle.jdbc.OracleDriver"
                Config.OracleDBConfig.ORACLE_JDBC_URL,  # "jdbc:oracle:thin:@//oracle-oltp:1521/ORCLPDB1"
                [Config.OracleDBConfig.ORACLE_USERNAME, Config.OracleDBConfig.ORACLE_PASSWORD],
                Config.OracleDBConfig.ORACLE_JDBC_DRIVER_PATH  # "/opt/spark/jars/ojdbc8.jar"
            )

            # if connect succeessfully, run a SQL
            with conn.cursor() as curs:
                curs.execute("SELECT 1 FROM DUAL")
                row = curs.fetchone()
                logging.info(f"Smars Debug======>>>>>>>: Successfully retrieved row: {row}")
            conn.close()

            # No Exception, means Connected
            logging.info("Smars Debug======>>>>>>>: Oracle Database Connected!")
            return True
        except Exception as e:
            logging.error(f"Smars Debug======>>>>>>>failed to connect Oracle Database: {e}")
            return False


class HDFSUtils:
    """Utility class for HDFS operations."""

    @staticmethod
    def check_hdfs_path(hdfs_path: str):
        """
        Check if the given HDFS path exists.

        Args:
            hdfs_path (str): The HDFS path to check.

        Returns:
            bool: True if the path exists, False otherwise.
        """

        try:
            # Construct the HDFS command
            cmd = f"hdfs dfs -ls {hdfs_path}"

            # Execute the command using subprocess
            result: subprocess.CompletedProcess = subprocess.run(
                cmd,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            logging.smars(f"Smars Debug======>>>>>>>: HDFS is existing: {hdfs_path}")
            return True

        except subprocess.CalledProcessError:
            logging.warning(f"Smars Debug======>>>>>>>: HDFS is non-existing: {hdfs_path}")
            return False


class LoggingUtils:
    """Utility class for customized logging operations."""

    @staticmethod
    def setup_custom_logger(log_name:str, log_level:int, level_name:str):
        """
        Setup a customized logger with a new log level.

        Args:
            log_name(str) : Custom log name. Use the file name `__name__` by default
            log_level (int): Custom log level (e.g., 25).
            level_name (str): Name for the custom log level.

        Returns:
            logging.Logger: Configured logger instance.
        """

        # Register the new log level
        logging.addLevelName(log_level, level_name)

        # customize logging method: for logger.smars_dev("log content")
        # bind the smars_dev() to Logger Class
        def smars_dev(self, message, *args, **kwargs):
            """
            Custom log function bound to logging.Logger.
            Logs messages at the specified custom log level.

            Args:
                self (logging.Logger): Logger instance.
                message (str): Log message.
                *args: Additional arguments.
                **kwargs: Additional keyword arguments.
            """
            if self.isEnabledFor(log_level):
                self._log(log_level, message, args, **kwargs)

        # Attach the custom logging method to the Logger class dynamically
        setattr(logging.Logger, level_name.lower(), smars_dev)

        # Config the certain logger level for its format, handlers etc.
        logging.basicConfig(
            level=log_level,
            format="%(asctime)s - %(name)s - %(levelname)s: - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[logging.StreamHandler()]  # Console output handler
        )

        # Return the logger instance for the current module with custom name
        return logging.getLogger(log_name)
#%%
