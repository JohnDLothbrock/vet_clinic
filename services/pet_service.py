from models.pet import Pet
from exceptions.owner_not_found_exception import (
    OwnerNotFoundException
)
from exceptions.pet_not_found_exception import (
    PetNotFoundException
)
from utils.logger import logger
from validators.pet_validator import (
    PetValidator
)


class PetService:


    def __init__(
        self,
        pet_repository,
        owner_service
    ):
        self.pet_repository = pet_repository
        self.owner_service = owner_service


    # CREATE
    def create_pet(
        self,
        pet: Pet
    ) -> None:

        owner = self.owner_service.get_owner_by_id(
            pet.owner_id
        )
        PetValidator.validate(
            pet.name,
            pet.species,
            pet.age
        )

        if owner is None:

            logger.warning(
                f"Invalid owner ID: {pet.owner_id}"
            )

            raise OwnerNotFoundException(
                pet.owner_id
            )
        self.pet_repository.create(pet)

        logger.info(
            f"Pet created: {pet.name}"
        )


    # READ
    def get_all_pets(self) -> list[Pet]:
        return self.pet_repository.get_all()


    # READ BY ID
    def get_pet_by_id(
            self,
            pet_id
    ):

        pet = self.pet_repository.get_by_id(
            pet_id
        )

        if not pet:
            logger.warning(
                f"Pet ID {pet_id} not found"
            )

            raise PetNotFoundException(
                pet_id
            )
        return pet


    # UPDATE
    def update_pet(
        self,
        pet_id: int,
        name: str,
        species: str,
        age: int
    ) -> None:

        pet = self.pet_repository.get_by_id(
            pet_id
        )
        if pet is None:
            logger.warning(
                f"Pet ID {pet_id} not found"
            )
            raise PetNotFoundException(
                pet_id
            )
        PetValidator.validate(
            name,
            species,
            age
        )

        self.pet_repository.update(
            pet_id,
            name,
            species,
            age
        )

        logger.info(
            f"Pet updated: {pet_id}"
        )


    # DELETE
    def delete_pet(
        self,
        pet_id: int
    ) -> None:

        pet = self.pet_repository.get_by_id(
            pet_id
        )

        if pet is None:
            logger.warning(
                f"Pet ID {pet_id} not found"
            )
            raise PetNotFoundException(
                pet_id
            )

        self.pet_repository.delete(
            pet_id
        )
        logger.info(
            f"Pet deleted: {pet_id}"
        )


    def search_pets_by_name(
            self,
            name
    ):
        logger.info(
            f"Searching pets by name: {name}"
        )
        return self.pet_repository.get_by_name(
            name
        )


    def get_all_pets_with_owner(self):

        return (
            self.pet_repository
            .get_all_with_owner()
        )

    def get_pets_by_owner_id(
            self,
            owner_id
    ):

        return (
            self.pet_repository.get_by_owner_id(
                owner_id
            )
        )