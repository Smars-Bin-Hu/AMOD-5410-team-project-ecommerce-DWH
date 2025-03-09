"""
    Importing Modules
    Layer1 : import standard modules or third party modules from project_directory/__init__.py
    Layer2 : import external modules in the project from project_directory.ext_mod/__init__.py
    Layer3 : import internal modules in the project from project_directory.int_mod/mod_file.py: avoid circular importing
"""
from .get_env import get_env

class HadoopEnvConfig:
    @staticmethod
    def get_hadoop_host():
        return get_env("HADOOP_HOST")

    @staticmethod
    def get_hadoop_user():
        return get_env("HADOOP_USER")

    @staticmethod
    def get_hive_ods_hdfs_path():
        return get_env("HIVE_ODS_HDFS_PATH")

    @staticmethod
    def get_jdbc_driver_path():
        return get_env("HADOOP_CLUSTER_ORACLE_JDBC_DRIVER_PATH")