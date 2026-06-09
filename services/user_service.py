from repositories.user_repository import UserRepository


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

    def update_password(
            self,
            user_id,
            password_hash
    ):

        self.user_repository.update_password(
            user_id,
            password_hash
        )