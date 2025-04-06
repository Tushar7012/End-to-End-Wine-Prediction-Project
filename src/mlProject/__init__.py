import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
)
   # Add handlers separately
file_handler = logging.FileHandler(log_filepath)
stream_handler = logging.StreamHandler(sys.stdout)

logger = logging.getLogger("mlProjectLogger")
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
