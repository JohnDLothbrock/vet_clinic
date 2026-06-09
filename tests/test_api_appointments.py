from fastapi.testclient import TestClient

from main_api import app

client = TestClient(app)


def get_auth_headers():

    response = client.post(
        "/api/v1/auth/login",
        json={
            "username": "admin",
            "password": "admin123"
        }
    )

    assert response.status_code == 200

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }


def test_get_appointments():

    response = client.get(
        "/api/v1/appointments",
        headers=get_auth_headers()
    )

    assert response.status_code == 200


def test_get_appointments_with_pet():

    response = client.get(
        "/api/v1/appointments/with-pet",
        headers=get_auth_headers()
    )

    assert response.status_code == 200