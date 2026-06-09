from repositories.user_repository import UserRepository

from models.user import User

from auth.password_utils import (
    hash_password,
    verify_password
)

from auth.roles import (
    ADMIN_ROLE_ID,
    VETERINARIAN_ROLE_ID,
    RECEPTIONIST_ROLE_ID
)

from exceptions.application_exception import (
    ApplicationException
)


class UserService:

    def __init__(
            self,
            user_repository: UserRepository
    ):

        self.user_repository = user_repository

    def get_user_by_username(
            self,
            username
    ):

        return (
            self.user_repository
            .get_by_username(
                username
            )
        )

    def get_user_by_email(
            self,
            email
    ):

        return (
            self.user_repository
            .get_by_email(
                email
            )
        )

    def get_user_by_id(
            self,
            user_id
    ):

        user = (
            self.user_repository
            .get_by_id(
                user_id
            )
        )

        if not user:

            raise ApplicationException(
                "User not found",
                404
            )

        return user

    def get_all_users(self):

        return (
            self.user_repository
            .get_all()
        )

    def create_user(
            self,
            username,
            email,
            password,
            role_id
    ):

        self._validate_role(
            role_id
        )

        self._validate_password(
            password
        )

        existing_username = (
            self.user_repository
            .get_by_username(
                username
            )
        )

        if existing_username:

            raise ApplicationException(
                "Username already exists",
                400
            )

        existing_email = (
            self.user_repository
            .get_by_email(
                email
            )
        )

        if existing_email:

            raise ApplicationException(
                "Email already exists",
                400
            )

        password_hash = hash_password(
            password
        )

        user = User(
            username=username,
            email=email,
            password_hash=password_hash,
            role_id=role_id,
            active=True
        )

        return (
            self.user_repository
            .create(
                user
            )
        )

    def update_password(
            self,
            user_id,
            password_hash
    ):

        self.user_repository.update_password(
            user_id,
            password_hash
        )

    def change_password(
            self,
            user_id,
            current_password,
            new_password
    ):

        user = self.get_user_by_id(
            user_id
        )

        if not verify_password(
                current_password,
                user.password_hash
        ):

            raise ApplicationException(
                "Current password is incorrect",
                400
            )

        self._validate_password(
            new_password
        )

        new_password_hash = hash_password(
            new_password
        )

        self.user_repository.update_password(
            user_id,
            new_password_hash
        )

        return {
            "message": "Password changed successfully"
        }

    def update_user_role(
            self,
            user_id,
            role_id
    ):

        self._validate_role(
            role_id
        )

        self.get_user_by_id(
            user_id
        )

        self.user_repository.update_role(
            user_id,
            role_id
        )

        return user_id

    def update_user_active(
            self,
            user_id,
            active
    ):

        self.get_user_by_id(
            user_id
        )

        self.user_repository.update_active(
            user_id,
            active
        )

        return user_id

    def _validate_role(
            self,
            role_id
    ):

        valid_roles = [
            ADMIN_ROLE_ID,
            VETERINARIAN_ROLE_ID,
            RECEPTIONIST_ROLE_ID
        ]

        if role_id not in valid_roles:

            raise ApplicationException(
                "Invalid role",
                400
            )

    def _validate_password(
            self,
            password
    ):

        if len(password) < 8:

            raise ApplicationException(
                "Password must contain at least 8 characters",
                400
            )