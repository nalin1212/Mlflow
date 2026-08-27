import os 
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the yaml file.

    Raises:
        ValueError: If the yaml file is empty.
        e: Empty file.

    Returns:
        ConfigBox:ConfigBox Type 


    """
    try:
        with open(path_to_yaml, encoding="utf-8") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is empty") from e
    except Exception as e:
        raise e
@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """Create directories if they do not already exist."""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Save a dictionary as a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load a JSON file and return its contents as a ConfigBox object."""
    with open(path, "r", encoding="utf-8") as f:
        content = json.load(f)
    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)   
@ensure_annotations
def save_bin(data: Any, path: Path):                    
    """Save data as a binary file using joblib."""
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:    
    """Load a binary file using joblib and return its contents."""
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data 
@ensure_annotations
def get_size(path: Path) -> str:    
    """Get the size of a file in kilobytes."""
    size_in_kb = round(os.path.getsize(path) / 1024)
    logger.info(f"Size of file at {path}: {size_in_kb} KB")
    return f"{size_in_kb} KB"

       
