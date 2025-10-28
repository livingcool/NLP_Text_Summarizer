from textSummarizer import config
from textSummarizer.compenents.Data_Transformation import DataTransformation
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
       config = ConfigurationManager()
    
    # 2. Get the specific configuration for Data Transformation
       data_transformation_config = config.get_data_transformation_config()
    
    # 3. Initialize the Data Transformation Component
       data_transformation = DataTransformation(config=data_transformation_config)
    
    # 4. Execute the transformation method
       data_transformation.convert()