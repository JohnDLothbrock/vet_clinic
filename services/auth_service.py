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

        print("=" * 50)
        print("LOGIN ATTEMPT")
        print("USERNAME RECEIVED:", username)

        user = (
            self.user_service
            .get_user_by_username(
                username
            )
        )

        print("USER FOUND:", user)

        if user:

            print("DB USERNAME:", user.username)
            print("DB HASH:", user.password_hash)
            print(
                "PASSWORD MATCH:",
                verify_password(
                    password,
                    user.password_hash
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
                "sub": user.username,
                "role_id": user.role_id
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }