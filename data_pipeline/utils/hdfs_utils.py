"""
    Importing Modules
    Layer1 : from project_directory import standard modules or third party modules
    Layer2 : from project_directory.ext_mod import external modules in the project
    Layer3 : import internal_modules ----- avoid circular importing
"""
import subprocess
from data_pipeline.configs import LoggingConfig
from .logging_utils import LoggingUtils

# create a logger for current util
smars_dev_log_level = int(LoggingConfig.get_smars_dev_log_level())
smars_dev_log_level_name = LoggingConfig.get_smars_dev_log_level_name()
logger = LoggingUtils.setup_custom_logger(
    "HDFS_UTILS_LOGGER",
    smars_dev_log_level,
    smars_dev_log_level_name
)

class HDFSUtils:
    """Utility class for HDFS operations."""

    @staticmethod
    def check_hdfs_path(hdfs_path: str) -> bool:
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
            logger.smars_dev(f"HDFS is existing: {hdfs_path}")
            return True
        except subprocess.CalledProcessError:
            logger.smars_dev(f"HDFS is non-existing: {hdfs_path}")
            return False