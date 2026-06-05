import pytest
from services.pet_service import PetService
from exceptions.pet_not_found_exception import PetNotFoundException
from models.pet import Pet

# Fake dependencies
class FakePetRepository:

    def get_by_id(self, pet_id):
        if pet_id == 1:
            return Pet("Max", "Dog", 3, 1, pet_id=1)
        return None

    def update(self, pet_id, name, species, age):
        pass

    def delete(self, pet_id):
        pass

    def get_by_name_with_owner(self, name):
        return []

    def get_all_with_owner(self):
        return []

    def get_by_owner_id(self, owner_id):
        return []

class FakeOwnerService:
    def get_owner_by_id(self, owner_id):
        return {"id": owner_id}


# Tests
def test_update_pet_success():
    service = PetService(FakePetRepository(), FakeOwnerService())
    service.update_pet(1, "Rocky", "Dog", 4)

def test_update_pet_not_found():
    service = PetService(FakePetRepository(), FakeOwnerService())
    with pytest.raises(PetNotFoundException):
        service.update_pet(999, "Rocky", "Dog", 4)

def test_delete_pet_success():
    service = PetService(FakePetRepository(), FakeOwnerService())
    service.delete_pet(1)

def test_delete_pet_not_found():
    service = PetService(FakePetRepository(), FakeOwnerService())
    with pytest.raises(PetNotFoundException):
        service.delete_pet(999)