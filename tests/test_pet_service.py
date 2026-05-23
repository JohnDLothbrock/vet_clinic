import pytest

from services.pet_service import PetService
from models.pet import Pet
from exceptions.owner_not_found_exception import (
    OwnerNotFoundException
)



#FAKE DEPENDENCIES FOR TESTING
class FakePetRepository:

    def create(self, pet):
        pass


class FakeOwnerService:

    def get_owner_by_id(self, owner_id):
        return None


class ValidOwnerService:

    def get_owner_by_id(self, owner_id):
        return {
            "id": owner_id,
            "name": "Juan"
        }


class TrackingPetRepository:

    def __init__(self):
        self.was_called = False

    def create(self, pet):
        self.was_called = True


# TESTS
def test_create_pet_with_invalid_owner():

    pet_repository = FakePetRepository()

    owner_service = FakeOwnerService()

    pet_service = PetService(
        pet_repository,
        owner_service
    )

    pet = Pet(
        "Max",
        "Dog",
        3,
        999
    )

    with pytest.raises(
        OwnerNotFoundException
    ):

        pet_service.create_pet(pet)


def test_create_pet_successfully():

    pet_repository = (
        TrackingPetRepository()
    )

    owner_service = (
        ValidOwnerService()
    )

    pet_service = PetService(
        pet_repository,
        owner_service
    )

    pet = Pet(
        "Max",
        "Dog",
        3,
        1
    )

    pet_service.create_pet(pet)

    assert (
        pet_repository.was_called
        is True
    )