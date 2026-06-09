from services.user_service import (
    UserService
)

from auth.password_utils import (
    verify_password
)

from auth.jwt_handler import (
    create_access_token
)

from exceptions.application_exception import (
    ApplicationException
)


class AuthService:

    def __init__(
            self,
            user_service: UserService
    ):

        self.user_service = user_service

    def login(
            self,
            username: str,
            password: str
    ):

        user = (
            self.user_service
            .get_user_by_username(
                username
            )
        )

        if not user:

            raise ApplicationException(
                "Invalid username or password",
                401
            )

        if not verify_password(
                password,
                user.password_hash
        ):

            raise ApplicationException(
                "Invalid username or password",
                401
            )

        token = create_access_token(
            {
                "user_id": user.id,
                "sub": user.username,
                "role_id": user.role_id
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }