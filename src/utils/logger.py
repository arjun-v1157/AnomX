# src/utils/logger.py

import logging
import sys

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    # Prevent adding multiple handlers if get_logger is called repeatedly
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False

    return logger