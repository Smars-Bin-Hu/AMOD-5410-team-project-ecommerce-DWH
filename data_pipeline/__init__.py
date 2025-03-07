import os
from pyspark.sql import SparkSession
from dotenv import load_dotenv
from pathlib import Path

# @desc :
__coding__ = "utf-8"
__author__ = "Smars Hu"
__date__ = "05 Mar 2025"

"""Loading Spark Session"""
spark = SparkSession.builder \
    .appName("etl_oracle_to_hdfs_pyspark_on_yarn") \
    .getOrCreate()

"""Load environment variables from .env and .env.secret file"""
# get the file path
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"
SECRET_ENV_FILE = BASE_DIR / ".env.secret"

# loading the env variable
load_dotenv(ENV_FILE)       # non-secret
load_dotenv(SECRET_ENV_FILE)    # secret

def get_env(key: str, default_value=None):
    """Get environment variable with a fallback default value"""
    return os.getenv(key, default_value)