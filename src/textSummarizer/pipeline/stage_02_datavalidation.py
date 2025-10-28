from textSummarizer import config
from textSummarizer.compenents.Data_Validation import DataValiadition
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
       config = ConfigurationManager()
    
    # 2. Get the specific configuration for Data Validation
       data_validation_config = config.get_data_validation_config()
    
    # 3. Initialize the Data Validation Component
    # Note: Class name is DataValiadition (as per your image, likely a typo for DataValidation)
       data_validation = DataValiadition(config=data_validation_config)
    
    # 4. Execute the Data Validation step
       data_validation.validate_all_files_exist()