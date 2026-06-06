from datetime import (
    datetime,
    timedelta,
    UTC
)

from jose import jwt

from config.settings import (
    JWT_SECRET,
    JWT_ALGORITHM
)

TOKEN_EXPIRE_MINUTES = 60


def create_access_token(
        data: dict
):

    payload = data.copy()

    expire = (
        datetime.now(
            UTC
        ) +
        timedelta(
            minutes=TOKEN_EXPIRE_MINUTES
        )
    )

    payload.update(
        {
            "exp": expire
        }
    )

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )