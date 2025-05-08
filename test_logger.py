import logging
import os
import sys

# Logger setup
log_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_file = os.path.join(log_dir, "test_log.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ],
    force=True
)

logger = logging.getLogger("testLogger")
logger.info("Test log message")
print("Test script ran")
