from fastapi.testclient import TestClient

from main_api import app

from app.dependencies import (
    get_user_service
)

from auth.current_user import (
    require_admin,
    require_authenticated_user
)

from models.user import User


client = TestClient(app)


class FakeUserService:

    def get_all_users(
            self
    ):

        return [
            User(
                user_id=1,
                username="admin",
                email="admin@vetclinic.com",
                password_hash="hash",
                role_id=1,
                active=True
            ),
            User(
                user_id=2,
                username="vet1",
                email="vet1@vetclinic.com",
                password_hash="hash",
                role_id=2,
                active=True
            )
        ]

    def get_user_by_id(
            self,
            user_id
    ):

        return User(
            user_id=user_id,
            username="admin",
            email="admin@vetclinic.com",
            password_hash="hash",
            role_id=1,
            active=True
        )

    def create_user(
            self,
            username,
            email,
            password,
            role_id
    ):

        return 10

    def update_user_role(
            self,
            user_id,
            role_id
    ):

        return user_id

    def update_user_active(
            self,
            user_id,
            active
    ):

        return user_id

    def change_password(
            self,
            user_id,
            current_password,
            new_password
    ):

        return {
            "message": "Password changed successfully"
        }


def fake_admin_user():

    return {
        "user_id": 1,
        "sub": "admin",
        "role_id": 1
    }


def fake_authenticated_user():

    return {
        "user_id": 1,
        "sub": "admin",
        "role_id": 1
    }


def setup_function():

    app.dependency_overrides.clear()

    app.dependency_overrides[
        get_user_service
    ] = lambda: FakeUserService()

    app.dependency_overrides[
        require_admin
    ] = fake_admin_user

    app.dependency_overrides[
        require_authenticated_user
    ] = fake_authenticated_user


def teardown_function():

    app.dependency_overrides.clear()


def test_get_users():

    response = client.get(
        "/api/v1/users"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2
    assert data[0]["username"] == "admin"
    assert data[1]["role_id"] == 2


def test_get_user_by_id():

    response = client.get(
        "/api/v1/users/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["username"] == "admin"


def test_create_user():

    response = client.post(
        "/api/v1/users",
        json={
            "username": "vet1",
            "email": "vet1@vetclinic.com",
            "password": "vet12345",
            "role_id": 2
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["message"] == "User created successfully"
    assert data["data"]["id"] == 10


def test_update_user_role():

    response = client.put(
        "/api/v1/users/2/role",
        json={
            "role_id": 3
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["message"] == "User role updated successfully"
    assert data["data"]["id"] == 2


def test_update_user_active():

    response = client.put(
        "/api/v1/users/2/active",
        json={
            "active": False
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["message"] == "User active status updated successfully"
    assert data["data"]["id"] == 2


def test_change_my_password():

    response = client.put(
        "/api/v1/users/me/change-password",
        json={
            "current_password": "oldPassword123",
            "new_password": "newPassword123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert (
        data["message"] ==
        "Password changed successfully"
    )