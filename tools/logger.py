import logging
from typing import Literal


def init_logger(name: str, level: int | Literal["DEBUG", "INFO", "WARNING", "ERROR"] = logging.INFO):

    if isinstance(level, str):
        level = getattr(logging, level)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
    logger.addHandler(handler)
    return logger


def logger_decor(func, logger, operation: str):
    def inner(cls, *args, **kwargs):
        logger.info(f'operation {operation} started.')
        func(cls, *args, **kwargs)
        logger.info(f'operation {operation} ended.')
    return classmethod(inner)
