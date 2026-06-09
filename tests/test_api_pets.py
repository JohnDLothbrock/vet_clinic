from types import SimpleNamespace

from fastapi.testclient import TestClient

from main_api import app

from app.dependencies import (
    get_pet_service
)

from auth.current_user import (
    require_authenticated_user,
    require_admin,
    require_admin_or_receptionist
)


client = TestClient(app)


class FakePetService:

    def get_all_pets(self):

        return [
            SimpleNamespace(
                id=1,
                name="Max",
                species="Dog",
                age=5,
                owner_id=1
            )
        ]

    def get_all_pets_with_owner(self):

        return [
            {
                "id": 1,
                "name": "Max",
                "species": "Dog",
                "age": 5,
                "owner_id": 1,
                "owner_name": "Juan"
            }
        ]

    def search_pets_by_name(
            self,
            name
    ):

        return [
            {
                "id": 1,
                "name": "Max",
                "species": "Dog",
                "age": 5,
                "owner_id": 1,
                "owner_name": "Juan"
            }
        ]


def fake_current_user():

    return {
        "user_id": 1,
        "sub": "admin",
        "role_id": 1
    }


app.dependency_overrides[
    get_pet_service
] = lambda: FakePetService()

app.dependency_overrides[
    require_authenticated_user
] = fake_current_user

app.dependency_overrides[
    require_admin
] = fake_current_user

app.dependency_overrides[
    require_admin_or_receptionist
] = fake_current_user


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