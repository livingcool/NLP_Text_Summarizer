from textSummarizer import config
from textSummarizer.compenents.Data_ingestion import DataIngestion
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
       config = ConfigurationManager()
    
    # 2. Get the specific configuration for Data Ingestion
       data_ingestion_config = config.get_data_ingestion_config()
    
    # 3. Initialize the Data Ingestion Component
       data_ingestion = DataIngestion(config=data_ingestion_config)
    
    # 4. Execute the Data Ingestion steps
    # This must download the file completely!
       data_ingestion.download_file() 
    
    # This will now attempt to extract the newly downloaded file
       data_ingestion.extract_zip_file()