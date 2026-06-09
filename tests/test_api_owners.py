from fastapi.testclient import TestClient

from main_api import app

from app.dependencies import (
    get_owner_service
)

from auth.current_user import (
    require_authenticated_user
)

from models.owner import Owner


client = TestClient(app)


class FakeOwnerService:

    def get_all_owners(self):

        return [
            Owner(
                owner_id=1,
                name="Juan",
                phone="88888888"
            ),
            Owner(
                owner_id=2,
                name="Maria",
                phone="77777777"
            )
        ]

    def get_owner_by_id(
            self,
            owner_id
    ):

        return Owner(
            owner_id=owner_id,
            name="Juan",
            phone="88888888"
        )

    def search_owners_by_name(
            self,
            name
    ):

        return [
            Owner(
                owner_id=1,
                name="Juan",
                phone="88888888"
            )
        ]


def fake_authenticated_user():

    return {
        "user_id": 1,
        "sub": "admin",
        "role_id": 1
    }


def setup_function():

    app.dependency_overrides.clear()

    app.dependency_overrides[
        get_owner_service
    ] = lambda: FakeOwnerService()

    app.dependency_overrides[
        require_authenticated_user
    ] = fake_authenticated_user


def teardown_function():

    app.dependency_overrides.clear()


def test_get_owners():

    response = client.get(
        "/api/v1/owners"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2
    assert data[0]["id"] == 1
    assert data[0]["name"] == "Juan"


def test_get_owner_by_id():

    response = client.get(
        "/api/v1/owners/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Juan"


def test_search_owner():

    response = client.get(
        "/api/v1/owners/search/juan"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["name"] == "Juan"