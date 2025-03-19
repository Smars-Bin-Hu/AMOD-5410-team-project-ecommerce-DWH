"""
    Importing Modules
    Layer1 : from project_directory import standard modules or third party modules
    Layer2 : from project_directory.ext_mod import external module classes in the project
    Layer3 : from internal_modules import class ----- avoid circular importing
"""
import jaydebeapi
from data_pipeline.configs import (
    HadoopEnvConfig,
    DatabaseConnectionConfig
)
from .logging_utils import logger

class OracleDatabaseUtils:
    """Oracle Database Utils"""

    @staticmethod
    def test_oracle_connection(oracle_db_config, db : str, instance : str) -> bool:
        """
        Test Whether the Oracle Connection is successful
        1) Load Oracle JDBC driver
        2) Connect to Oracle
        3) Execute a simple query, e.g. SELECT 1 FROM DUAL
        4) Return True if no exception, otherwise return False
        """
        oracle_jdbc_url : str = oracle_db_config.get_jdbc_url(db,instance)
        oracle_properties : dict = oracle_db_config.get_properties(db,instance)
        
        try:
            logger.smars_dev("Attempting to connect to Oracle Database...")

            # connect the oracle
            conn = jaydebeapi.connect(
                "oracle.jdbc.OracleDriver",
                oracle_jdbc_url,
                [oracle_properties["user"],
                 oracle_properties["password"]],
                HadoopEnvConfig.get_jdbc_driver_path()
            )

            # if connect succeessfully, run a SQL
            with conn.cursor() as curs:
                curs.execute("SELECT 1 FROM DUAL")
                row = curs.fetchone()
                logger.smars_dev(f"Successfully retrieved row: {row}")
            conn.close()

            # No Exception, means Connected
            logger.smars_dev("Oracle Database Connected!")
            return True
        except Exception as e:
            logger.smars_dev(f"failed to connect Oracle Database: {e}")
            return False