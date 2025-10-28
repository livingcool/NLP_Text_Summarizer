import os
from transformers import AutoTokenizer
from datasets import load_from_disk
from textSummarizer.logging import logger
from pathlib import Path
from typing import Dict, Any, Union
from textSummarizer.entity import DataTransformationConfig
# Assuming DataTransformationConfig is imported from .entity
# Example: from textSummarizer.entity import DataTransformationConfig

class DataTransformation:
    """
    A component class to handle tokenization and transformation 
    of the dataset for the model training stage.
    """
    def __init__(self, config: DataTransformationConfig):
        # Stores the configuration object (data paths, tokenizer name)
        self.config = config
        
        # Load the tokenizer specified in the configuration
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    def convert_examples_to_features(self, example_batch: Dict[str, Union[list, Any]]):
        """
        Tokenizes an example batch of the dataset.

        Args:
            example_batch (Dict): A batch dictionary from the dataset (e.g., {'dialogue': [...], 'summary': [...]}).

        Returns:
            Dict: A dictionary containing tokenized inputs, labels, and attention masks.
        """
        # Tokenize the input text (dialogue)
        # Max length of 1024 tokens for input dialogue
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)

        # Tokenize the target summary (labels)
        with self.tokenizer.as_target_tokenizer():
            # Max length of 128 tokens for target summary
            target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation=True)

        # Create the dictionary of features for the model (input_ids, attention_mask, and labels)
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert(self):
        """
        Loads the dataset from disk, tokenizes it using the mapping function, 
        and saves the tokenized dataset to a new location.
        """
        logger.info(f"Loading dataset from: {self.config.data_path}")
        # Load the dataset saved in the previous stage
        dataset_samsum = load_from_disk(self.config.data_path)
        
        logger.info("Starting dataset tokenization...")
        # Apply the tokenization function (convert_examples_to_features)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)
        
        # Save the tokenized, processed dataset
        save_path = os.path.join(self.config.root_dir, "samsum_dataset")
        dataset_samsum_pt.save_to_disk(save_path)
        logger.info(f"Tokenized dataset saved to: {save_path}")