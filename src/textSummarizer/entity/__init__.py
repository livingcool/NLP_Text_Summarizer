from dataclasses import dataclass
from pathlib import Path

# The @dataclass(frozen=True) decorator automatically generates methods like __init__, __repr__, etc.
# frozen=True makes the instances immutable (read-only) after creation.
@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Defines the structure for Data Ingestion configuration.
    The types match the values read from the config.yaml file.
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen=True)
class DataValidationConfig:
    """
    Defines the structure for Data Validation configuration.
    This entity holds the paths and parameters needed for the validation step.
    """
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list[str]
    
@dataclass(frozen=True)
class DataTransformationConfig:
    """
    Defines the structure for Data Transformation configuration.
    Note: The 'tokenizer_name' is typed as Path in the image, 
    but for a Hugging Face model name, 'str' is usually more appropriate.
    """
    root_dir: Path
    data_path: Path
    tokenizer_name: Path
    
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int