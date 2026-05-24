import logging

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
    "vet_clinic.log"
)

file_handler.setFormatter(
    formatter
)

console_handler = logging.StreamHandler()

console_handler.setFormatter(
    formatter
)

logger.addHandler(
    file_handler
)

logger.addHandler(
    console_handler
)