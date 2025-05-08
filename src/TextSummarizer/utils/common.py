import os
from box.exceptions import BoxValueError  # for catching YAML format errors
import yaml  # for reading YAML files
from TextSummarizer.logging import logger  # custom logger to show logs in terminal + file
from ensure import ensure_annotations  # ensures we follow type hints strictly
from box import ConfigBox  # allows dot-access to dictionary keys
from pathlib import Path  # handles file paths cleanly
from typing import Any  # for type hinting (not used directly here)


#  Reads a YAML file and returns its contents as a ConfigBox (dict with dot access)
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox.
    
    Args:
        path_to_yaml (Path): path to the YAML file

    Raises:
        ValueError: if the YAML file is empty
        e: for any unexpected error

    Returns:
        ConfigBox: dictionary-like object with dot-access
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)  # load YAML as Python dict
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)  # return as dot-accessible object
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


#  Creates directories given a list of paths
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create folders from a list of paths.
    
    Args:
        path_to_directories (list): list of folder paths
        verbose (bool): whether to print log messages
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # safely create folder
        if verbose:
            logger.info(f"Created directory at: {path}")


#  Returns size of a file in KB
@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size of a file in kilobytes.

    Args:
        path (Path): path to the file

    Returns:
        str: file size in KB, formatted as string
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # get size in KB
    return f"~ {size_in_kb} KB"
