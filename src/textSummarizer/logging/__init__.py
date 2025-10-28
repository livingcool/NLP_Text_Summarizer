import os
import sys
import logging

# Define the log message format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the log directory and file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Basic configuration for logging
logging.basicConfig(
    level=logging.INFO, # Set the minimum level of messages to process (INFO, WARNING, ERROR, etc.)
    format=logging_str, # Apply the defined format string
    
    # Define handlers to direct log messages to multiple destinations
    handlers=[
        # 1. FileHandler: Writes logs to the specified file
        logging.FileHandler(log_filepath),
        
        # 2. StreamHandler: Writes logs to the console (standard output)
        logging.StreamHandler(sys.stdout)
    ]
)

# Get a custom logger instance for your application
logger = logging.getLogger("textSummarizerLogger")

# Example usage:
# logger.info("Log setup completed successfully.")
# logger.warning("This is a warning message.")