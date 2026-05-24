from models.pet import Pet
from services.pet_service import PetService
from views.pet_view import PetView
from services.owner_service import OwnerService
from exceptions.owner_not_found_exception import (
    OwnerNotFoundException
)
from repositories.pet_repository import (
    PetRepository
)
from repositories.owner_repository import (
    OwnerRepository
)
from exceptions.pet_not_found_exception import (
    PetNotFoundException
)


class PetController:


    def __init__(
        self,
        pet_service
    ):
        self.pet_service = pet_service
        self.pet_view = PetView()


    def create_pet(self):

        name, species, age, owner_id = (
            self.pet_view.get_pet_data()
        )

        pet = Pet(
            name,
            species,
            age,
            owner_id
        )

        try:
            self.pet_service.create_pet(pet)
            print("Pet added successfully.")

        except OwnerNotFoundException as error:
            print(error)


    def show_pets(self) -> None:
        pets = self.pet_service.get_all_pets()

        self.pet_view.display_pets(pets)


    def update_pet(self):
        try:

            (
                pet_id,
                name,
                species,
                age
            ) = self.pet_view.get_pet_update_data()

            self.pet_service.update_pet(
                pet_id,
                name,
                species,
                age
            )

            print(
                "Pet updated successfully."
            )

        except PetNotFoundException as error:

            print(error)


    def delete_pet(self):
        try:

            pet_id = (
                self.pet_view.get_pet_id()
            )

            self.pet_service.delete_pet(
                pet_id
            )

            print(
                "Pet deleted successfully."
            )

        except PetNotFoundException as error:

            print(error)