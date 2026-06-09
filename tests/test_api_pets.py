from fastapi.testclient import TestClient

from main_api import app

from app.dependencies import (
    get_pet_service
)

from auth.current_user import (
    require_authenticated_user
)

from models.pet import Pet


client = TestClient(app)


class FakePetService:

    def get_all_pets(self):

        return [
            Pet(
                pet_id=1,
                name="Max",
                species="Dog",
                age=5,
                owner_id=1
            ),
            Pet(
                pet_id=2,
                name="Luna",
                species="Cat",
                age=3,
                owner_id=2
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
            },
            {
                "id": 2,
                "name": "Luna",
                "species": "Cat",
                "age": 3,
                "owner_id": 2,
                "owner_name": "Maria"
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


def fake_authenticated_user():

    return {
        "user_id": 1,
        "sub": "admin",
        "role_id": 1
    }


def setup_function():

    app.dependency_overrides.clear()

    app.dependency_overrides[
        get_pet_service
    ] = lambda: FakePetService()

    app.dependency_overrides[
        require_authenticated_user
    ] = fake_authenticated_user


def teardown_function():

    app.dependency_overrides.clear()


def test_get_pets():

    response = client.get(
        "/api/v1/pets"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2
    assert data[0]["id"] == 1
    assert data[0]["name"] == "Max"


def test_get_pets_with_owner():

    response = client.get(
        "/api/v1/pets/with-owner"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2
    assert data[0]["owner_name"] == "Juan"


def test_search_pet():

    response = client.get(
        "/api/v1/pets/search/max"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["name"] == "Max"