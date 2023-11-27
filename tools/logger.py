import logging
from typing import Literal


def init_logger(name: str, level: int | Literal["DEBUG", "INFO", "WARNING", "ERROR"] = logging.INFO):

    if isinstance(level, str):
        level = getattr(logging, level)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(levelname)s - %(name)s - %(message)s'))
    logger.addHandler(handler)
    return logger
