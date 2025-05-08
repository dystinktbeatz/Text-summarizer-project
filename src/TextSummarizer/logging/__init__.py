import os
import sys
import logging

# Log message format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Log file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),       # Log to file
        logging.StreamHandler(sys.stdout)        # Log to console
    ],
    force=True  # Force reconfiguration if logging was already set
)

# Create a reusable logger instance
logger = logging.getLogger("textSummarizerLogger")
