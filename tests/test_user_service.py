from types import SimpleNamespace

import pytest

from auth.password_utils import (
    hash_password
)

from exceptions.application_exception import (
    ApplicationException
)

from models.user import User

from services.user_service import (
    UserService
)


class FakeUserRepository:

    def __init__(
            self
    ):

        self.users = []
        self.created_user = None
        self.updated_password = None
        self.updated_role = None
        self.updated_active = None

    def get_by_username(
            self,
            username
    ):

        for user in self.users:

            if user.username == username:

                return user

        return None

    def get_by_email(
            self,
            email
    ):

        for user in self.users:

            if user.email == email:

                return user

        return None

    def get_by_id(
            self,
            user_id
    ):

        for user in self.users:

            if user.id == user_id:

                return user

        return None

    def get_all(
            self
    ):

        return self.users

    def create(
            self,
            user: User
    ):

        self.created_user = user

        return 10

    def update_password(
            self,
            user_id,
            password_hash
    ):

        self.updated_password = {
            "user_id": user_id,
            "password_hash": password_hash
        }

    def update_role(
            self,
            user_id,
            role_id
    ):

        self.updated_role = {
            "user_id": user_id,
            "role_id": role_id
        }

    def update_active(
            self,
            user_id,
            active
    ):

        self.updated_active = {
            "user_id": user_id,
            "active": active
        }


def test_get_all_users_returns_users():

    repository = FakeUserRepository()

    repository.users = [
        User(
            user_id=1,
            username="admin",
            email="admin@vetclinic.com",
            password_hash="hash",
            role_id=1,
            active=True
        )
    ]

    service = UserService(
        repository
    )

    users = service.get_all_users()

    assert len(users) == 1
    assert users[0].username == "admin"


def test_create_user_success():

    repository = FakeUserRepository()

    service = UserService(
        repository
    )

    user_id = service.create_user(
        username="vet1",
        email="vet1@vetclinic.com",
        password="vet12345",
        role_id=2
    )

    assert user_id == 10
    assert repository.created_user is not None
    assert repository.created_user.username == "vet1"
    assert repository.created_user.email == "vet1@vetclinic.com"
    assert repository.created_user.role_id == 2
    assert repository.created_user.active is True


def test_create_user_duplicate_username_raises_exception():

    repository = FakeUserRepository()

    repository.users = [
        User(
            user_id=1,
            username="vet1",
            email="existing@vetclinic.com",
            password_hash="hash",
            role_id=2,
            active=True
        )
    ]

    service = UserService(
        repository
    )

    with pytest.raises(
        ApplicationException
    ) as exception:

        service.create_user(
            username="vet1",
            email="new@vetclinic.com",
            password="vet12345",
            role_id=2
        )

    assert exception.value.status_code == 400
    assert exception.value.message == "Username already exists"


def test_create_user_duplicate_email_raises_exception():

    repository = FakeUserRepository()

    repository.users = [
        User(
            user_id=1,
            username="vet1",
            email="vet1@vetclinic.com",
            password_hash="hash",
            role_id=2,
            active=True
        )
    ]

    service = UserService(
        repository
    )

    with pytest.raises(
        ApplicationException
    ) as exception:

        service.create_user(
            username="vet2",
            email="vet1@vetclinic.com",
            password="vet12345",
            role_id=2
        )

    assert exception.value.status_code == 400
    assert exception.value.message == "Email already exists"


def test_create_user_invalid_role_raises_exception():

    repository = FakeUserRepository()

    service = UserService(
        repository
    )

    with pytest.raises(
        ApplicationException
    ) as exception:

        service.create_user(
            username="user1",
            email="user1@vetclinic.com",
            password="user12345",
            role_id=99
        )

    assert exception.value.status_code == 400
    assert exception.value.message == "Invalid role"


def test_create_user_short_password_raises_exception():

    repository = FakeUserRepository()

    service = UserService(
        repository
    )

    with pytest.raises(
        ApplicationException
    ) as exception:

        service.create_user(
            username="user1",
            email="user1@vetclinic.com",
            password="short",
            role_id=2
        )

    assert exception.value.status_code == 400
    assert (
        exception.value.message ==
        "Password must contain at least 8 characters"
    )


def test_change_password_success():

    repository = FakeUserRepository()

    repository.users = [
        User(
            user_id=1,
            username="admin",
            email="admin@vetclinic.com",
            password_hash=hash_password(
                "oldPassword123"
            ),
            role_id=1,
            active=True
        )
    ]

    service = UserService(
        repository
    )

    response = service.change_password(
        user_id=1,
        current_password="oldPassword123",
        new_password="newPassword123"
    )

    assert (
        response["message"] ==
        "Password changed successfully"
    )

    assert repository.updated_password is not None
    assert repository.updated_password["user_id"] == 1


def test_change_password_wrong_current_password_raises_exception():

    repository = FakeUserRepository()

    repository.users = [
        User(
            user_id=1,
            username="admin",
            email="admin@vetclinic.com",
            password_hash=hash_password(
                "oldPassword123"
            ),
            role_id=1,
            active=True
        )
    ]

    service = UserService(
        repository
    )

    with pytest.raises(
        ApplicationException
    ) as exception:

        service.change_password(
            user_id=1,
            current_password="wrongPassword",
            new_password="newPassword123"
        )

    assert exception.value.status_code == 400
    assert exception.value.message == "Current password is incorrect"


def test_update_user_role_success():

    repository = FakeUserRepository()

    repository.users = [
        User(
            user_id=1,
            username="vet1",
            email="vet1@vetclinic.com",
            password_hash="hash",
            role_id=2,
            active=True
        )
    ]

    service = UserService(
        repository
    )

    updated_user_id = service.update_user_role(
        user_id=1,
        role_id=3
    )

    assert updated_user_id == 1
    assert repository.updated_role["user_id"] == 1
    assert repository.updated_role["role_id"] == 3


def test_update_user_active_success():

    repository = FakeUserRepository()

    repository.users = [
        User(
            user_id=1,
            username="vet1",
            email="vet1@vetclinic.com",
            password_hash="hash",
            role_id=2,
            active=True
        )
    ]

    service = UserService(
        repository
    )

    updated_user_id = service.update_user_active(
        user_id=1,
        active=False
    )

    assert updated_user_id == 1
    assert repository.updated_active["user_id"] == 1
    assert repository.updated_active["active"] is False