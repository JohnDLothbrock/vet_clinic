from repositories.owner_repository import (
    OwnerRepository
)


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