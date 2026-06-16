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
            owner_repository: OwnerRepository,
            audit_log_service=None
    ):

        self.owner_repository = (
            owner_repository
        )

        self.audit_log_service = (
            audit_log_service
        )

        self.pet_service = None

    def create_owner(
            self,
            owner,
            user_id=None
    ) -> int:

        OwnerValidator.validate(
            owner.name,
            owner.phone
        )

        owner_id = (
            self.owner_repository.create(
                owner
            )
        )

        if self.audit_log_service and user_id:

            self.audit_log_service.create_audit_log(
                user_id=user_id,
                action="CREATE",
                entity="Owner",
                entity_id=owner_id
            )

        logger.info(
            f"Owner created: {owner.name}"
        )

        return owner_id

    def get_all_owners(self):

        return (
            self.owner_repository.get_all()
        )

    def get_paginated_owners(
            self,
            page: int,
            page_size: int,
            search: str | None = None
    ):

        logger.info(
            "Fetching paginated owners"
        )

        if page < 1:

            page = 1

        if page_size < 1:

            page_size = 10

        if page_size > 100:

            page_size = 100

        return (
            self.owner_repository
            .get_paginated(
                page=page,
                page_size=page_size,
                search=search
            )
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
            phone,
            user_id=None
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

        if self.audit_log_service and user_id:

            self.audit_log_service.create_audit_log(
                user_id=user_id,
                action="UPDATE",
                entity="Owner",
                entity_id=owner_id
            )

        logger.info(
            f"Owner updated: {owner_id}"
        )

        return owner_id

    def delete_owner(
            self,
            owner_id,
            user_id=None
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

        if self.audit_log_service and user_id:

            self.audit_log_service.create_audit_log(
                user_id=user_id,
                action="DELETE",
                entity="Owner",
                entity_id=owner_id
            )

        logger.info(
            f"Owner deleted: {owner_id}"
        )

        return owner_id

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