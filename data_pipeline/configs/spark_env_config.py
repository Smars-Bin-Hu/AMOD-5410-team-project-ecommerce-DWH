"""
    Importing Modules
    Layer1 : import standard modules or third party modules from project_directory/__init__.py
    Layer2 : import external modules in the project from project_directory.ext_mod/__init__.py
    Layer3 : import internal modules in the project from project_directory.int_mod/mod_file.py: avoid circular importing
"""
from data_pipeline import get_env

# class SparkEnvConfig:
#     # @staticmethod
#     # def get_hadoop_host():
#     #     return get_env("SPARK_APP_NAME")
