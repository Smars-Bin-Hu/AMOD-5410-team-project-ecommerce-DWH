"""
    Importing Modules
    Layer1 : import standard modules or third party modules from project_directory/__init__.py
    Layer2 : import external modules in the project from project_directory.ext_mod/__init__.py
    Layer3 : import internal modules in the project from project_directory.int_mod/mod_file.py: avoid circular importing
"""
from .get_env import get_env

class LoggingConfig:
    @staticmethod
    def get_smars_dev_log_level():
        return get_env("SMARS_DEV_LOG_LEVEL")

    @staticmethod
    def get_smars_dev_log_level_name():
        return get_env("SMARS_DEV_LOG_LEVEL_NAME")
