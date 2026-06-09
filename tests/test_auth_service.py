from types import SimpleNamespace

import pytest

from auth.password_utils import (
    hash_password
)

from exceptions.application_exception import (
    ApplicationException
)

from services.auth_service import (
    AuthService
)


class FakeUserService:

    def __init__(
            self,
            user=None
    ):

        self.user = user

    def get_user_by_username(
            self,
            username
    ):

        return self.user


def test_login_success_returns_token():

    user = SimpleNamespace(
        id=1,
        username="admin",
        email="admin@vetclinic.com",
        password_hash=hash_password(
            "admin12345"
        ),
        role_id=1,
        active=True
    )

    auth_service = AuthService(
        FakeUserService(
            user
        )
    )

    response = auth_service.login(
        "admin",
        "admin12345"
    )

    assert "access_token" in response
    assert response["token_type"] == "bearer"


def test_login_invalid_username_raises_exception():

    auth_service = AuthService(
        FakeUserService(
            None
        )
    )

    with pytest.raises(
        ApplicationException
    ) as exception:

        auth_service.login(
            "wrong_user",
            "admin12345"
        )

    assert exception.value.status_code == 401
    assert (
        exception.value.message ==
        "Invalid username or password"
    )


def test_login_invalid_password_raises_exception():

    user = SimpleNamespace(
        id=1,
        username="admin",
        email="admin@vetclinic.com",
        password_hash=hash_password(
            "admin12345"
        ),
        role_id=1,
        active=True
    )

    auth_service = AuthService(
        FakeUserService(
            user
        )
    )

    with pytest.raises(
        ApplicationException
    ) as exception:

        auth_service.login(
            "admin",
            "wrong_password"
        )

    assert exception.value.status_code == 401
    assert (
        exception.value.message ==
        "Invalid username or password"
    )


def test_login_inactive_user_raises_exception():

    user = SimpleNamespace(
        id=1,
        username="admin",
        email="admin@vetclinic.com",
        password_hash=hash_password(
            "admin12345"
        ),
        role_id=1,
        active=False
    )

    auth_service = AuthService(
        FakeUserService(
            user
        )
    )

    with pytest.raises(
        ApplicationException
    ) as exception:

        auth_service.login(
            "admin",
            "admin12345"
        )

    assert exception.value.status_code == 403
    assert (
        exception.value.message ==
        "User account is inactive"
    )