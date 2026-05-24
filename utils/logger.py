import logging

from config.settings import LOG_FILE

logger = logging.getLogger(
    "vet_clinic"
)

logger.setLevel(
    logging.INFO
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler = logging.FileHandler(
    LOG_FILE
)

file_handler.setFormatter(
    formatter
)

console_handler = logging.StreamHandler()

console_handler.setFormatter(
    formatter
)

if not logger.handlers:

    logger.addHandler(
        file_handler
    )

    logger.addHandler(
        console_handler
    )