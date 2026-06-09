from utils.logger import logger

from config.settings import (
    APP_ENV
)


class EmailService:

    def send_password_reset_email(
            self,
            email,
            reset_link
    ):

        if APP_ENV == "development":

            logger.info(
                (
                    "Password reset email generated. "
                    f"Recipient: {email}. "
                    f"Reset link: {reset_link}"
                )
            )

            print("=" * 80)
            print("PASSWORD RESET LINK")
            print(f"Recipient: {email}")
            print(reset_link)
            print("=" * 80)

            return

        logger.info(
            (
                "Password reset email would be sent in production. "
                f"Recipient: {email}"
            )
        )