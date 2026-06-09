from datetime import (
    datetime,
    timedelta,
    UTC
)

from auth.password_utils import (
    hash_password
)

from auth.token_utils import (
    generate_secure_token,
    hash_token
)

from config.settings import (
    FRONTEND_URL,
    PASSWORD_RESET_EXPIRE_MINUTES
)

from models.password_reset_token import (
    PasswordResetToken
)

from utils.logger import logger

from exceptions.application_exception import (
    ApplicationException
)


class PasswordResetService:

    def __init__(
            self,
            user_service,
            password_reset_token_repository,
            email_service
    ):

        self.user_service = user_service

        self.password_reset_token_repository = (
            password_reset_token_repository
        )

        self.email_service = email_service

    def request_password_reset(
            self,
            email
    ):

        user = (
            self.user_service
            .get_user_by_email(
                email
            )
        )

        if not user:

            logger.warning(
                (
                    "Password reset requested for "
                    f"non-existing email: {email}"
                )
            )

            return {
                "message": (
                    "If the email exists, a password reset link "
                    "has been sent."
                )
            }

        if not user.active:

            logger.warning(
                (
                    "Password reset requested for inactive user: "
                    f"{email}"
                )
            )

            return {
                "message": (
                    "If the email exists, a password reset link "
                    "has been sent."
                )
            }

        self.password_reset_token_repository.expire_active_tokens_for_user(
            user.id
        )

        plain_token = generate_secure_token()

        token_hash = hash_token(
            plain_token
        )

        expires_at = (
            datetime.now(
                UTC
            ) +
            timedelta(
                minutes=PASSWORD_RESET_EXPIRE_MINUTES
            )
        ).replace(
            tzinfo=None
        )

        password_reset_token = PasswordResetToken(
            user_id=user.id,
            token_hash=token_hash,
            expires_at=expires_at
        )

        self.password_reset_token_repository.create(
            password_reset_token
        )

        reset_link = (
            f"{FRONTEND_URL}/reset-password"
            f"?token={plain_token}"
        )

        self.email_service.send_password_reset_email(
            user.email,
            reset_link
        )

        logger.info(
            f"Password reset requested for user ID {user.id}"
        )

        return {
            "message": (
                "If the email exists, a password reset link "
                "has been sent."
            )
        }

    def reset_password(
            self,
            token,
            new_password
    ):

        if len(new_password) < 8:

            raise ApplicationException(
                "Password must contain at least 8 characters",
                400
            )

        token_hash = hash_token(
            token
        )

        password_reset_token = (
            self.password_reset_token_repository
            .get_valid_by_token_hash(
                token_hash
            )
        )

        if not password_reset_token:

            raise ApplicationException(
                "Invalid or expired password reset token",
                400
            )

        new_password_hash = hash_password(
            new_password
        )

        self.user_service.update_password(
            password_reset_token.user_id,
            new_password_hash
        )

        self.password_reset_token_repository.mark_as_used(
            password_reset_token.id
        )

        logger.info(
            (
                "Password reset completed for user ID "
                f"{password_reset_token.user_id}"
            )
        )

        return {
            "message": "Password reset successfully"
        }