from types import SimpleNamespace

from fastapi.testclient import TestClient

from main_api import app

from app.dependencies import (
    get_owner_service
)

from auth.current_user import (
    require_authenticated_user,
    require_admin,
    require_admin_or_receptionist
)


client = TestClient(app)


class FakeOwnerService:

    def get_all_owners(self):

        return [
            SimpleNamespace(
                id=1,
                name="Juan",
                phone="88888888"
            )
        ]

    def get_owner_by_id(
            self,
            owner_id
    ):

        return SimpleNamespace(
            id=owner_id,
            name="Juan",
            phone="88888888"
        )

    def search_owners_by_name(
            self,
            name
    ):

        return [
            SimpleNamespace(
                id=1,
                name="Juan",
                phone="88888888"
            )
        ]


def fake_current_user():

    return {
        "user_id": 1,
        "sub": "admin",
        "role_id": 1
    }


app.dependency_overrides[
    get_owner_service
] = lambda: FakeOwnerService()

app.dependency_overrides[
    require_authenticated_user
] = fake_current_user

app.dependency_overrides[
    require_admin
] = fake_current_user

app.dependency_overrides[
    require_admin_or_receptionist
] = fake_current_user


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