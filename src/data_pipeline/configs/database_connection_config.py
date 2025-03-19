"""
    Importing Modules
    Layer1 : import standard modules or third party modules from project_directory/__init__.py
    Layer2 : import external modules in the project from project_directory.ext_mod/__init__.py
    Layer3 : import internal modules in the project from project_directory.int_mod/mod_file.py: avoid circular importing
"""
from .get_env import get_env

class DatabaseConnectionConfig:
    """Database Configuration Singleton: Supports multiple databases"""

    _instances = {}

    def __new__(cls, db_type: str, db_instance_code: str):
        """Ensure only one instance per database type"""
        key = f"{db_type.lower()}_{db_instance_code}"
        if key not in cls._instances:
            cls._instances[key] = super(DatabaseConnectionConfig, cls).__new__(cls)
        return cls._instances[key]

    def __init__(self, db_type: str, db_instance_code : str):
        """Initialize configuration only if not set before"""
        if not hasattr(self, "_initialized"):  # avoid __init__ to be used again
            self.db_type = db_type.lower()

        # Oracle Database
        # instance code == 1
        if self.db_type == "oracle" and db_instance_code == "1":
            # self._jdbc_driver_path = get_env("ORACLE_JDBC_DRIVER_PATH")
            self._host = get_env("ORACLE_HOST")
            self._port = get_env("ORACLE_PORT")
            self._service_name = get_env("ORACLE_SERVICE_NAME")
            self._username = get_env("ORACLE_USERNAME")
            self._password = get_env("ORACLE_PASSWORD")
            self._jdbc_url = f"jdbc:oracle:thin:@//{self._host}:{self._port}/{self._service_name}"

        # Clickhouse Database
        if self.db_type == "clickhouse" and db_instance_code == "1":
            self._host = get_env("CLICKHOUSE_HOST")
            self._port = get_env("CLICKHOUSE_PORT")
            self._username = get_env("CLICKHOUSE_USER")
            self._password = get_env("CLICKHOUSE_PASSWORD")

        self._initialized = True  # marked as initialized

    def get_jdbc_url(self, db_type: str, db_instance_code : str):
        """Getter: the JDBC URL"""
        if  db_type == "oracle" and db_type == self.db_type and db_instance_code == "1":
            return self._jdbc_url
        if  db_type == "clickhouse" and db_type == self.db_type and db_instance_code == "1":
            return None

    def get_properties(self, db_type: str, db_instance_code : str):
        """Getter: Return the connection properties"""
        if  db_type == "oracle" and db_instance_code == "1":
            return {
                "user": self._username,
                "password": self._password,
                "driver": "oracle.jdbc.OracleDriver" # for Spark connect Oracle
            }
        if  db_type == "clickhouse" and db_instance_code == "1":
            return {
                "user": self._username,
                "password": self._password,
                "port": self._port,
                "host": self._host
            }