from datetime import (
    datetime,
    timedelta
)

from types import SimpleNamespace

import pytest

from auth.token_utils import (
    hash_token
)

from exceptions.application_exception import (
    ApplicationException
)

from models.password_reset_token import (
    PasswordResetToken
)

from services.password_reset_service import (
    PasswordResetService
)


class FakeUserService:

    def __init__(
            self,
            user=None
    ):

        self.user = user
        self.updated_user_id = None
        self.updated_password_hash = None

    def get_user_by_email(
            self,
            email
    ):

        return self.user

    def update_password(
            self,
            user_id,
            password_hash
    ):

        self.updated_user_id = user_id
        self.updated_password_hash = password_hash


class FakePasswordResetTokenRepository:

    def __init__(
            self,
            reset_token=None
    ):

        self.reset_token = reset_token
        self.created_token = None
        self.expired_user_id = None
        self.used_token_id = None

    def expire_active_tokens_for_user(
            self,
            user_id
    ):

        self.expired_user_id = user_id

    def create(
            self,
            password_reset_token
    ):

        self.created_token = password_reset_token

        return 1

    def get_valid_by_token_hash(
            self,
            token_hash
    ):

        if (
            self.reset_token and
            self.reset_token.token_hash == token_hash
        ):

            return self.reset_token

        return None

    def mark_as_used(
            self,
            password_reset_token_id
    ):

        self.used_token_id = (
            password_reset_token_id
        )


class FakeEmailService:

    def __init__(self):

        self.email = None
        self.reset_link = None

    def send_password_reset_email(
            self,
            email,
            reset_link
    ):

        self.email = email
        self.reset_link = reset_link


def test_request_password_reset_existing_active_user_creates_token_and_sends_email():

    user = SimpleNamespace(
        id=1,
        email="admin@vetclinic.com",
        active=True
    )

    user_service = FakeUserService(
        user
    )

    token_repository = (
        FakePasswordResetTokenRepository()
    )

    email_service = FakeEmailService()

    password_reset_service = PasswordResetService(
        user_service,
        token_repository,
        email_service
    )

    response = (
        password_reset_service
        .request_password_reset(
            "admin@vetclinic.com"
        )
    )

    assert (
        response["message"] ==
        "If the email exists, a password reset link has been sent."
    )

    assert token_repository.expired_user_id == 1
    assert token_repository.created_token is not None
    assert token_repository.created_token.user_id == 1

    assert email_service.email == "admin@vetclinic.com"
    assert "/reset-password?token=" in email_service.reset_link


def test_request_password_reset_non_existing_user_returns_safe_message():

    user_service = FakeUserService(
        None
    )

    token_repository = (
        FakePasswordResetTokenRepository()
    )

    email_service = FakeEmailService()

    password_reset_service = PasswordResetService(
        user_service,
        token_repository,
        email_service
    )

    response = (
        password_reset_service
        .request_password_reset(
            "missing@vetclinic.com"
        )
    )

    assert (
        response["message"] ==
        "If the email exists, a password reset link has been sent."
    )

    assert token_repository.created_token is None
    assert email_service.email is None


def test_request_password_reset_inactive_user_returns_safe_message():

    user = SimpleNamespace(
        id=1,
        email="admin@vetclinic.com",
        active=False
    )

    user_service = FakeUserService(
        user
    )

    token_repository = (
        FakePasswordResetTokenRepository()
    )

    email_service = FakeEmailService()

    password_reset_service = PasswordResetService(
        user_service,
        token_repository,
        email_service
    )

    response = (
        password_reset_service
        .request_password_reset(
            "admin@vetclinic.com"
        )
    )

    assert (
        response["message"] ==
        "If the email exists, a password reset link has been sent."
    )

    assert token_repository.created_token is None
    assert email_service.email is None


def test_reset_password_success_updates_password_and_marks_token_used():

    plain_token = "valid-reset-token"

    reset_token = PasswordResetToken(
        password_reset_token_id=1,
        user_id=10,
        token_hash=hash_token(
            plain_token
        ),
        expires_at=datetime.now() +
        timedelta(
            minutes=30
        ),
        used=False
    )

    user_service = FakeUserService()

    token_repository = (
        FakePasswordResetTokenRepository(
            reset_token
        )
    )

    email_service = FakeEmailService()

    password_reset_service = PasswordResetService(
        user_service,
        token_repository,
        email_service
    )

    response = password_reset_service.reset_password(
        plain_token,
        "newPassword123"
    )

    assert (
        response["message"] ==
        "Password reset successfully"
    )

    assert user_service.updated_user_id == 10
    assert user_service.updated_password_hash is not None
    assert token_repository.used_token_id == 1


def test_reset_password_invalid_token_raises_exception():

    user_service = FakeUserService()

    token_repository = (
        FakePasswordResetTokenRepository()
    )

    email_service = FakeEmailService()

    password_reset_service = PasswordResetService(
        user_service,
        token_repository,
        email_service
    )

    with pytest.raises(
        ApplicationException
    ) as exception:

        password_reset_service.reset_password(
            "invalid-token",
            "newPassword123"
        )

    assert exception.value.status_code == 400
    assert (
        exception.value.message ==
        "Invalid or expired password reset token"
    )


def test_reset_password_short_password_raises_exception():

    user_service = FakeUserService()

    token_repository = (
        FakePasswordResetTokenRepository()
    )

    email_service = FakeEmailService()

    password_reset_service = PasswordResetService(
        user_service,
        token_repository,
        email_service
    )

    with pytest.raises(
        ApplicationException
    ) as exception:

        password_reset_service.reset_password(
            "valid-token",
            "short"
        )

    assert exception.value.status_code == 400
    assert (
        exception.value.message ==
        "Password must contain at least 8 characters"
    )