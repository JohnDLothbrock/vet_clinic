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

DB_USERNAME = os.getenv(
    "DB_USERNAME"
)

DB_PASSWORD = os.getenv(
    "DB_PASSWORD"
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

JWT_SECRET = os.getenv(
    "JWT_SECRET"
)

JWT_ALGORITHM = os.getenv(
    "JWT_ALGORITHM",
    "HS256"
)

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

JWT_SECRET = os.getenv(
    "JWT_SECRET"
)

JWT_ALGORITHM = os.getenv(
    "JWT_ALGORITHM",
    "HS256"
)