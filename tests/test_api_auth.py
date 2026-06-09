from fastapi.testclient import TestClient

from main_api import app

from app.dependencies import (
    get_auth_service,
    get_password_reset_service
)


client = TestClient(app)


class FakeAuthService:

    def login(
            self,
            username,
            password
    ):

        return {
            "access_token": "fake-token",
            "token_type": "bearer"
        }


class FakePasswordResetService:

    def request_password_reset(
            self,
            email
    ):

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

        return {
            "message": "Password reset successfully"
        }


def setup_function():

    app.dependency_overrides.clear()

    app.dependency_overrides[
        get_auth_service
    ] = lambda: FakeAuthService()

    app.dependency_overrides[
        get_password_reset_service
    ] = lambda: FakePasswordResetService()


def teardown_function():

    app.dependency_overrides.clear()


def test_login_endpoint():

    response = client.post(
        "/api/v1/auth/login",
        json={
            "username": "admin",
            "password": "admin12345"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["access_token"] == "fake-token"
    assert data["token_type"] == "bearer"


def test_forgot_password_endpoint():

    response = client.post(
        "/api/v1/auth/forgot-password",
        json={
            "email": "admin@vetclinic.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert (
        data["message"] ==
        "If the email exists, a password reset link has been sent."
    )


def test_reset_password_endpoint():

    response = client.post(
        "/api/v1/auth/reset-password",
        json={
            "token": "fake-reset-token",
            "new_password": "admin12345"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert (
        data["message"] ==
        "Password reset successfully"
    )