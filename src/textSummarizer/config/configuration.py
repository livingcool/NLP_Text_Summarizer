from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml,create_directories
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.entity import DataValidationConfig,DataTransformationConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        # Load configurations using the read_yaml utility
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Ensure the main artifacts root directory exists
        create_directories([self.config.artifacts_root])

    # Method to get the Data Ingestion specific configuration
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir]) # Create ingestion root directory

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        """Reads data_validation configuration from config.yaml
        and returns it as a DataValidationConfig object."""
    # 1. Access the 'data_validation' section of the main configuration
        config = self.config.data_validation

    # 2. Create the root directory for data validation artifacts
    # Assumes create_directories is available (e.g., imported from utils.common)
        create_directories([config.root_dir])

    # 3. Create the DataValidationConfig entity object
        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir), # Convert string path to Path object
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

    # 4. Return the configured object
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Reads data_transformation configuration from config.yaml
        and returns it as a DataTransformationConfig object.
        """
        # 1. Access the 'data_transformation' section
        config = self.config.data_transformation

        # 2. Create the root directory for data transformation artifacts
        create_directories([config.root_dir])

        # 3. Create the DataTransformationConfig entity object
        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path),
            tokenizer_name=config.tokenizer_name
        )

        # 4. Return the configured object
        return data_transformation_config