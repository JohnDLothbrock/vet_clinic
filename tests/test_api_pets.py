from fastapi.testclient import TestClient

from main_api import app

client = TestClient(app)


def test_get_pets():

    response = client.get(
        "/api/v1/pets"
    )

    assert response.status_code == 200


def test_get_pets_with_owner():

    response = client.get(
        "/api/v1/pets/with-owner"
    )

    assert response.status_code == 200


def test_search_pet():

    response = client.get(
        "/api/v1/pets/search/max"
    )

    assert response.status_code == 200