import logging
import sys
import subprocess

# get logger
logger = logging.getLogger(__name__)

# creat formatter
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)

# create handler
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('app.log')

# set formatter
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# add handler to the logger
logger.handlers = [stream_handler, file_handler]

# set log-level
logger.setLevel(logging.INFO)
