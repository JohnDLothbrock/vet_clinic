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


def test_get_owners():

    response = client.get(
        "/api/v1/owners",
        headers=get_auth_headers()
    )

    assert response.status_code == 200


def test_get_owner_by_id():

    response = client.get(
        "/api/v1/owners/1",
        headers=get_auth_headers()
    )

    assert response.status_code in [
        200,
        404
    ]


def test_search_owner():

    response = client.get(
        "/api/v1/owners/search/juan",
        headers=get_auth_headers()
    )

    assert response.status_code == 200