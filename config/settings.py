from dotenv import load_dotenv
import os

load_dotenv()


def get_env_value(
        key,
        default=None
):

    value = os.getenv(
        key,
        default
    )

    return value


def get_env_list(
        key,
        default_value
):

    raw_value = os.getenv(
        key,
        default_value
    )

    return [
        item.strip()
        for item in raw_value.split(",")
        if item.strip()
    ]


DB_SERVER = get_env_value(
    "DB_SERVER"
)

DB_DATABASE = get_env_value(
    "DB_DATABASE"
)

DB_DRIVER = get_env_value(
    "DB_DRIVER"
)

DB_USERNAME = get_env_value(
    "DB_USERNAME"
)

DB_PASSWORD = get_env_value(
    "DB_PASSWORD"
)

LOG_FILE = get_env_value(
    "LOG_FILE",
    "vet_clinic.log"
)

APP_NAME = get_env_value(
    "APP_NAME",
    "Veterinary Clinic"
)

APP_ENV = get_env_value(
    "APP_ENV",
    "development"
)

JWT_SECRET = get_env_value(
    "JWT_SECRET",
    "development-secret-key-change-this"
)

JWT_ALGORITHM = get_env_value(
    "JWT_ALGORITHM",
    "HS256"
)

FRONTEND_URL = get_env_value(
    "FRONTEND_URL",
    "http://localhost:5173"
)

CORS_ORIGINS = get_env_list(
    "CORS_ORIGINS",
    "http://localhost:5173,http://127.0.0.1:5173"
)

PASSWORD_RESET_EXPIRE_MINUTES = int(
    get_env_value(
        "PASSWORD_RESET_EXPIRE_MINUTES",
        "30"
    )
)

OPENAI_API_KEY = get_env_value(
    "OPENAI_API_KEY"
)


if (
    APP_ENV == "production" and
    JWT_SECRET == "development-secret-key-change-this"
):

    raise ValueError(
        "JWT_SECRET must be configured in production."
    )