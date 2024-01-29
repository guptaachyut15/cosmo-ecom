import os
import logging
from dotenv import load_dotenv
from constants.logging import LoggerConstant

load_dotenv()
logging.basicConfig(level=logging.INFO)


def get_config(name):
    return os.getenv(name)


MONGODB_URL = get_config("MONGODB_URL")
LOG = logging.getLogger(LoggerConstant.logger_name)
