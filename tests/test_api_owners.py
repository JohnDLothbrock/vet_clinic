from fastapi.testclient import TestClient

from main_api import app

from app.dependencies import get_owner_service


class MockOwnerService:

    def get_all_owners(self):
        return []

    def get_owner_by_id(self, owner_id):
        return {
            "id": owner_id,
            "name": "Juan",
            "phone": "88888888"
        }

    def search_owners_by_name(self, name):
        return []


app.dependency_overrides[
    get_owner_service
] = lambda: MockOwnerService()

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

    assert response.status_code == 200


def test_search_owner():

    response = client.get(
        "/api/v1/owners/search/juan"
    )

    assert response.status_code == 200