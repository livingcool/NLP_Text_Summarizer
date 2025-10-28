import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig


# Assuming DataIngestionConfig is imported or defined earlier
# Example: from textSummarizer.entity import DataIngestionConfig 
# (You would need to ensure this import is present in your actual file)

class DataIngestion:
    """
    A component class to handle the data downloading and storage.
    """
    def __init__(self, config: DataIngestionConfig):
        # Store the immutable configuration object
        self.config = config

    def download_file(self):
        """
        Downloads the file from the source URL if it doesn't already exist locally.
        """
        # Check if the local data file path exists
        if not os.path.exists(self.config.local_data_file):
            
            # If it doesn't exist, download the file using urllib.request.urlretrieve
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            # If the file already exists, log its size
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
            
    # CORRECTED: This method is now properly indented within the DataIngestion class.
    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory.
        """
        # Get the target directory for unzipping from the configuration
        unzip_path = self.config.unzip_dir
        
        # Ensure the destination directory exists
        os.makedirs(unzip_path, exist_ok=True)
        
        # Open the local zip file and extract all contents to the unzip_path
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            
        logger.info(f"Extracted zip file to: {unzip_path}")