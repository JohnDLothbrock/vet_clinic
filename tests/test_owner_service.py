import pytest

from services.owner_service import OwnerService
from models.owner import Owner

from exceptions.owner_not_found_exception import (
    OwnerNotFoundException
)

from exceptions.owner_has_pets_exception import (
    OwnerHasPetsException
)



# FAKES / testing

class FakeOwnerRepository:

    def __init__(self):

        self.owner = None
        self.deleted = False
        self.updated = False

    def create(self, owner):

        self.owner = owner

    def get_by_id(self, owner_id):

        return self.owner

    def update(self, owner):

        self.updated = True

    def delete(self, owner_id):

        self.deleted = True


class FakePetServiceNoPets:

    def get_pets_by_owner_id(
        self,
        owner_id
    ):

        return []


class FakePetServiceWithPets:

    def get_pets_by_owner_id(
        self,
        owner_id
    ):

        return ["pet"]


# --------------------
# TESTS
# --------------------

def test_create_owner():

    repo = FakeOwnerRepository()

    service = OwnerService(
        repo
    )

    owner = Owner(
        "Juan",
        "88888888"
    )

    service.create_owner(
        owner
    )

    assert repo.owner == owner


def test_get_owner_by_id_success():

    repo = FakeOwnerRepository()

    repo.owner = Owner(
        "Juan",
        "88888888",
        1
    )

    service = OwnerService(
        repo
    )

    owner = service.get_owner_by_id(
        1
    )

    assert owner.id == 1


def test_get_owner_by_id_not_found():

    repo = FakeOwnerRepository()

    service = OwnerService(
        repo
    )

    with pytest.raises(
        OwnerNotFoundException
    ):

        service.get_owner_by_id(
            999
        )


def test_delete_owner_success():

    repo = FakeOwnerRepository()

    repo.owner = Owner(
        "Juan",
        "88888888",
        1
    )

    service = OwnerService(
        repo
    )

    service.pet_service = (
        FakePetServiceNoPets()
    )

    service.delete_owner(
        1
    )

    assert repo.deleted is True


def test_delete_owner_with_pets():

    repo = FakeOwnerRepository()

    repo.owner = Owner(
        "Juan",
        "88888888",
        1
    )

    service = OwnerService(
        repo
    )

    service.pet_service = (
        FakePetServiceWithPets()
    )

    with pytest.raises(
        OwnerHasPetsException
    ):

        service.delete_owner(
            1
        )


def test_update_owner_success():

    repo = FakeOwnerRepository()

    repo.owner = Owner(
        "Juan",
        "88888888",
        1
    )

    service = OwnerService(
        repo
    )

    service.update_owner(
        1,
        "Pedro",
        "77777777"
    )

    assert repo.updated is True