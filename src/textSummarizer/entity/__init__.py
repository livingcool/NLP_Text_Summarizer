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