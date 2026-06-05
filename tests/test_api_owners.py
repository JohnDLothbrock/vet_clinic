from fastapi.testclient import TestClient

from main_api import app

client = TestClient(app)


def test_get_owners():

    response = client.get(
        "/api/v1/owners"
    )

    assert response.status_code == 200

def test_get_owner_by_id():

    response = client.get(
        "/api/v1/owners/1"
    )

    assert response.status_code in [
        200,
        404
    ]


def test_search_owner():

    response = client.get(
        "/api/v1/owners/search/juan"
    )

    assert response.status_code == 200