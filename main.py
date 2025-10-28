from textSummarizer.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_datavalidation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_datatransformation import DataTransformationTrainingPipeline
from textSummarizer.logging import logger

# Define the current stage name as a constant
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    
    # Initialize and run the Data Ingestion Pipeline
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================x")
    
except Exception as e:
    # Log the full traceback if an error occurs
    logger.exception(e)
    # Re-raise the exception to stop execution
    raise e

# Define the current stage name as a constant
STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    
    # Initialize and run the Data Ingestion Pipeline
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================x")
    
except Exception as e:
    # Log the full traceback if an error occurs
    logger.exception(e)
    # Re-raise the exception to stop execution
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    
    # Initialize and run the Data Ingestion Pipeline
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================x")
    
except Exception as e:
    # Log the full traceback if an error occurs
    logger.exception(e)
    # Re-raise the exception to stop execution
    raise e