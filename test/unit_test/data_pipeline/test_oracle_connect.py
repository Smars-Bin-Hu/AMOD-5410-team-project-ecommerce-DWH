import logging
# import config as cfg
import jaydebeapi  # all NodeManager need install this API

"""config"""
ORACLE_JDBC_DRIVER_PATH = "/opt/spark/jars/ojdbc8.jar"
ORACLE_HOST = "oracle-oltp"
ORACLE_PORT = "1521"
ORACLE_SERVICE_NAME = "ORCLPDB1"
ORACLE_USERNAME = "Smars"
ORACLE_PASSWORD = "Whos3301919!"
ORACLE_DRIVER = "oracle.jdbc.OracleDriver"
ORACLE_JDBC_URL = f"jdbc:oracle:thin:@//{ORACLE_HOST}:{ORACLE_PORT}/{ORACLE_SERVICE_NAME}"
print("debug111")

try:
    print("Attempting to connect to Oracle Database...")
    logging.info("Attempting to connect to Oracle Database...")

    # JayDeBeApi need driver class, JDBC url, username&password list, and JDBC Driver path
    conn = jaydebeapi.connect(
        ORACLE_DRIVER,           # "oracle.jdbc.OracleDriver"
        ORACLE_JDBC_URL,         # "jdbc:oracle:thin:@//oracle-oltp:1521/ORCLPDB1"
        [ORACLE_USERNAME, ORACLE_PASSWORD],
        ORACLE_JDBC_DRIVER_PATH  # "/opt/spark/jars/ojdbc8.jar"
    )

    # if connect succeessfully, run a SQL
    with conn.cursor() as curs:
        curs.execute("SELECT 1 FROM DUAL")
        row = curs.fetchone()
        # logging.info(f"Successfully retrieved row: {row}")
        print(f"Successfully retrieved row: {row}")
    conn.close()

    # No Exception, means Connected
    print("Debug: Oracle Database Connected!")
    # logging.info("Oracle Database Connected!")
except Exception as e:
    print(f"failed to connect Oracle Database: {e}")
    # logging.error(f"failed to connect Oracle Database: {e}")