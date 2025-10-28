import os
from pathlib import Path
import logging

# Configure logging to show information about file creation
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# --- Project Configuration ---
project_name = "textSummarizer"

# List of files and directories to be created (Consolidated from all images)
list_of_files = [
    # Files from the first image
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/compenents/__init__.py", # Note: 'compenents' is likely a typo for 'components'
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    
    # Files from the second image (continuation)
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]
# -----------------------------

# --- File and Directory Creation Logic ---
for filepath in list_of_files:
    # 1. Convert the string path to a Path object for OS-independent operations
    filepath = Path(filepath)

    # 2. Extract the directory (parent) and the file name
    filedir, filename = os.path.split(filepath)

    # --- Create Directory if it doesn't exist (if there's a directory part) ---
    if filedir != "":
        # Use os.makedirs with exist_ok=True to create nested directories safely
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    # --- Create File if it doesn't exist or is empty ---
    # Check if the file doesn't exist or its size is 0 bytes
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create an empty file
        with open(filepath, 'w') as f:
            pass # simply create and close the file
        logging.info(f"Creating empty file: {filepath}")
    else:
        # File already exists and is not empty
        logging.info(f"{filename} is already exists")