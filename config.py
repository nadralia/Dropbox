"""
Config file for the program. All constants should be stored here.
"""
import os

# Retrieves the dropbox API oauth 2 access token saved as an environment variable.
TOKEN = os.environ.get("ACCESS_TOKEN")
SOURCE_DIR = os.environ.get("SOURCE_DIR")