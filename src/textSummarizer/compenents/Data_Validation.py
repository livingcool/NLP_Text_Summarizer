from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig
import os
class DataValiadition:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    # Inside the DataValiadition class
    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None
            data_dir = os.path.join("artifacts", "data_ingestion", "samsum_dataset")
            all_files = os.listdir(data_dir)

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                # 📢 NEW LINE: Log the file causing the failure!
                    logger.warning(f"Validation failed! Unexpected file found: {file}")
                
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}\nFailing file: {file}")
                    break
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e