"""
config.py

Config Files, including Database, HDFS constant variable info

"""

# Oracle Database Configuration
ORACLE_JDBC_DRIVER_PATH = "/opt/sqoop/lib/ojdbc8.jar"
ORACLE_HOST = "172.18.0.10"
ORACLE_PORT = "1521"
ORACLE_SID = "ORCL"
ORACLE_USERNAME = "your_user"
ORACLE_PASSWORD = "your_password"
ORACLE_TABLE = "your_table"

# HDFS Target Path
HDFS_PATH = "/user/hdfs/oracle_data"

# Sqoop Command and Configuration
SQOOP_CMD_TEMPLATE = (
    "sqoop import --connect jdbc:oracle:thin:@{host}:{port}:{sid} "
    "--username {user} --password {password} "
    "--table {table} --target-dir {hdfs_path} "
    "--delete-target-dir --num-mappers 1 "
    "--driver oracle.jdbc.OracleDriver "
    "--as-parquetfile"
)

# Logging
LOG_FILE = "logs/etl_process.log"
