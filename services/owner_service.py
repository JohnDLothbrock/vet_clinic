from repositories.owner_repository import (
    OwnerRepository
)
from exceptions.owner_not_found_exception import OwnerNotFoundException


class OwnerService:

    def __init__(
            self,
            owner_repository: OwnerRepository
    ):
        self.owner_repository = owner_repository

    def create_owner(self, owner) -> None:
        self.owner_repository.create(owner)

    def get_all_owners(self):
        return self.owner_repository.get_all()

    def get_owner_by_id(self, owner_id):
        return self.owner_repository.get_by_id(owner_id)

    def update_owner(self, owner_id, name, phone):
        existing_owner = self.owner_repository.get_by_id(owner_id)

        if not existing_owner:
            raise OwnerNotFoundException(owner_id)

        updated_owner = Owner(
            name=name,
            phone=phone,
            owner_id=owner_id
        )

        self.owner_repository.update(updated_owner)

    def delete_owner(self, owner_id):

        existing_owner = self.owner_repository.get_by_id(owner_id)

        if not existing_owner:
            raise OwnerNotFoundException(owner_id)

        self.owner_repository.delete(owner_id)