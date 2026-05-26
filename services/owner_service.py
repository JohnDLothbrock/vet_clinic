from repositories.owner_repository import (
    OwnerRepository
)
from exceptions.owner_not_found_exception import OwnerNotFoundException
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
        self.owner_repository = owner_repository

    def create_owner(self, owner) -> None:
        
        OwnerValidator.validate(
            owner.name,
            owner.phone
        )

        self.owner_repository.create(owner)

        logger.info(
            f"Owner created: {owner.name}"
        )

    def get_all_owners(self):
        return self.owner_repository.get_all()

    def get_owner_by_id(self, owner_id):
        return self.owner_repository.get_by_id(owner_id)

    def update_owner(self, owner_id, name, phone):
        existing_owner = self.owner_repository.get_by_id(owner_id)

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

        self.owner_repository.update(updated_owner)

        logger.info(
            f"Owner updated: {owner_id}"
        )

    def delete_owner(self, owner_id):

        existing_owner = self.owner_repository.get_by_id(owner_id)

        if not existing_owner:
            logger.warning(
                f"Owner ID {owner_id} not found"
            )
            raise OwnerNotFoundException(
                owner_id
            )

        self.owner_repository.delete(owner_id)

        logger.info(
            f"Owner deleted: {owner_id}"
        )