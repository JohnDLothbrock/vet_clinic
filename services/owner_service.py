from repositories.owner_repository import (
    OwnerRepository
)

from exceptions.owner_not_found_exception import (
    OwnerNotFoundException
)

from exceptions.owner_has_pets_exception import (
    OwnerHasPetsException
)

from utils.logger import logger

from models.owner import Owner

from validators.owner_validator import (
    OwnerValidator
)


class OwnerService:

    def __init__(
            self,
            owner_repository: OwnerRepository
    ):

        self.owner_repository = (
            owner_repository
        )

        self.pet_service = None

    def create_owner(
            self,
            owner
    ) -> None:

        OwnerValidator.validate(
            owner.name,
            owner.phone
        )

        self.owner_repository.create(
            owner
        )

        logger.info(
            f"Owner created: {owner.name}"
        )

    def get_all_owners(self):

        return (
            self.owner_repository.get_all()
        )

    def get_owner_by_id(
            self,
            owner_id
    ):

        owner = self.owner_repository.get_by_id(
            owner_id
        )

        if not owner:

            logger.warning(
                f"Owner ID {owner_id} not found"
            )

            raise OwnerNotFoundException(
                owner_id
            )

        return owner

    def update_owner(
            self,
            owner_id,
            name,
            phone
    ):

        existing_owner = (
            self.owner_repository.get_by_id(
                owner_id
            )
        )

        if not existing_owner:

            logger.warning(
                f"Owner ID {owner_id} not found"
            )

            raise OwnerNotFoundException(
                owner_id
            )

        OwnerValidator.validate(
            name,
            phone
        )

        updated_owner = Owner(
            name=name,
            phone=phone,
            owner_id=owner_id
        )

        self.owner_repository.update(
            updated_owner
        )

        logger.info(
            f"Owner updated: {owner_id}"
        )

    def delete_owner(
            self,
            owner_id
    ):

        existing_owner = (
            self.owner_repository.get_by_id(
                owner_id
            )
        )

        if not existing_owner:

            logger.warning(
                f"Owner ID {owner_id} not found"
            )

            raise OwnerNotFoundException(
                owner_id
            )

        if self.pet_service:

            pets = (
                self.pet_service.get_pets_by_owner_id(
                    owner_id
                )
            )

            if len(pets) > 0:

                logger.warning(
                    f"Owner {owner_id} still has pets assigned"
                )

                raise OwnerHasPetsException(
                    owner_id
                )

        self.owner_repository.delete(
            owner_id
        )

        logger.info(
            f"Owner deleted: {owner_id}"
        )

    def search_owners_by_name(
            self,
            name
    ):

        logger.info(
            f"Searching owners by name: {name}"
        )

        return (
            self.owner_repository.get_by_name(
                name
            )
        )