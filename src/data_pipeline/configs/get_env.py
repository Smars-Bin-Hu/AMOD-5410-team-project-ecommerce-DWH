import os

def get_env(key: str, default_value=None):
    """Get environment variable with a fallback default value"""
    return os.getenv(key, default_value)