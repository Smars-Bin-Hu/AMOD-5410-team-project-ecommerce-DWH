"""
    Importing Modules
    Layer1 : from project_directory import standard modules or third party modules
    Layer2 : from project_directory.ext_mod import external modules in the project
    Layer3 : import internal_modules ----- avoid circular importing
"""
import subprocess
from .logging_utils import logger

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
            subprocess.run(
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