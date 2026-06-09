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


def test_get_pets():

    response = client.get(
        "/api/v1/pets",
        headers=get_auth_headers()
    )

    assert response.status_code == 200


def test_get_pets_with_owner():

    response = client.get(
        "/api/v1/pets/with-owner",
        headers=get_auth_headers()
    )

    assert response.status_code == 200


def test_search_pet():

    response = client.get(
        "/api/v1/pets/search/max",
        headers=get_auth_headers()
    )

    assert response.status_code == 200