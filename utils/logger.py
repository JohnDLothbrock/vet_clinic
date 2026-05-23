import logging

logging.basicConfig(
    filename="vet_clinic.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("vet_clinic")