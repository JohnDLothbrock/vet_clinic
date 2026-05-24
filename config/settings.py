from dotenv import load_dotenv
import os

load_dotenv()

DB_SERVER = os.getenv(
    "DB_SERVER"
)

DB_DATABASE = os.getenv(
    "DB_DATABASE"
)

DB_DRIVER = os.getenv(
    "DB_DRIVER"
)

LOG_FILE = os.getenv(
    "LOG_FILE",
    "vet_clinic.log"
)

APP_NAME = os.getenv(
    "APP_NAME",
    "Veterinary Clinic"
)

APP_ENV = os.getenv(
    "APP_ENV",
    "development"
)