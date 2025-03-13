# @Desc
__package__="batch_processing"
__author__ = "Smars Hu"
__date__ = "5 Mar 2025"
__version__ = "1.0"

from dotenv import load_dotenv
from pathlib import Path
import os
__all__ = ["jobs", "configs", "utils"]

"""Load environment variables from .env and .env.secret file"""
# get the file path
BASE_DIR = Path(__file__).resolve().parent / "configs"
ENV_FILE = BASE_DIR / ".env"

# loading the env variable
load_dotenv(ENV_FILE)       # non-secret