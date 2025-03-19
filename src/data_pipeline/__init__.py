# @Desc
__package__="data_pipeline"
__author__ = "Smars Hu"
__date__ = "28 Feb 2025"
__version__ = "1.0"

from dotenv import load_dotenv
from pathlib import Path
import os
__all__ = ["core", "configs", "utils"]

"""Load environment variables from .env and .env.secret file"""
# get the file p
BASE_DIR = Path(__file__).resolve().parent / "configs"
ENV_FILE = BASE_DIR / ".env"
SECRET_ENV_FILE = BASE_DIR / ".env.secret"

# loading the env variable
load_dotenv(ENV_FILE)       # non-secret
load_dotenv(SECRET_ENV_FILE)    # secret