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
            owner_service,
            audit_log_service=None
    ):

        self.pet_repository = pet_repository
        self.owner_service = owner_service
        self.audit_log_service = audit_log_service

    def create_pet(
            self,
            pet: Pet,
            user_id=None
    ) -> int:

        owner = (
            self.owner_service.get_owner_by_id(
                pet.owner_id
            )
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

        pet_id = (
            self.pet_repository.create(
                pet
            )
        )

        if self.audit_log_service and user_id:

            self.audit_log_service.create_audit_log(
                user_id=user_id,
                action="CREATE",
                entity="Pet",
                entity_id=pet_id
            )

        logger.info(
            f"Pet created: {pet.name}"
        )

        return pet_id

    def get_all_pets(
            self
    ) -> list[Pet]:

        return (
            self.pet_repository.get_all()
        )

    def get_pet_by_id(
            self,
            pet_id
    ):

        pet = (
            self.pet_repository.get_by_id(
                pet_id
            )
        )

        if not pet:

            logger.warning(
                f"Pet ID {pet_id} not found"
            )

            raise PetNotFoundException(
                pet_id
            )

        return pet

    def update_pet(
            self,
            pet_id: int,
            name: str,
            species: str,
            age: int,
            user_id=None
    ) -> int:

        pet = (
            self.pet_repository.get_by_id(
                pet_id
            )
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

        if self.audit_log_service and user_id:

            self.audit_log_service.create_audit_log(
                user_id=user_id,
                action="UPDATE",
                entity="Pet",
                entity_id=pet_id
            )

        logger.info(
            f"Pet updated: {pet_id}"
        )

        return pet_id

    def delete_pet(
            self,
            pet_id: int,
            user_id=None
    ) -> int:

        pet = (
            self.pet_repository.get_by_id(
                pet_id
            )
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

        if self.audit_log_service and user_id:

            self.audit_log_service.create_audit_log(
                user_id=user_id,
                action="DELETE",
                entity="Pet",
                entity_id=pet_id
            )

        logger.info(
            f"Pet deleted: {pet_id}"
        )

        return pet_id

    def search_pets_by_name(
            self,
            name
    ):

        logger.info(
            f"Searching pets by name: {name}"
        )

        return (
            self.pet_repository
            .get_by_name_with_owner(
                name
            )
        )

    def get_all_pets_with_owner(
            self
    ):

        return (
            self.pet_repository
            .get_all_with_owner()
        )

    def get_paginated_pets_with_owner(
            self,
            page: int,
            page_size: int,
            search: str | None = None,
            species: str | None = None,
            owner_id: int | None = None
    ):

        logger.info(
            "Fetching paginated pets with owner data"
        )

        if page < 1:

            page = 1

        if page_size < 1:

            page_size = 10

        if page_size > 100:

            page_size = 100

        return (
            self.pet_repository
            .get_paginated_with_owner(
                page=page,
                page_size=page_size,
                search=search,
                species=species,
                owner_id=owner_id
            )
        )

    def get_pets_by_owner_id(
            self,
            owner_id
    ):

        return (
            self.pet_repository
            .get_by_owner_id(
                owner_id
            )
        )