from models.owner import Owner
from services.owner_service import OwnerService
from views.owner_view import OwnerView
from repositories.owner_repository import (
    OwnerRepository
)


class OwnerController:

    def __init__(self):

        owner_repository = OwnerRepository()
        self.owner_service = OwnerService(
            owner_repository
        )
        self.owner_view = OwnerView()

    def create_owner(self):

        name, phone = self.owner_view.get_owner_data()
        owner = Owner(name, phone)
        self.owner_service.create_owner(owner)

    def show_owners(self):

        owners = self.owner_service.get_all_owners()
        self.owner_view.display_owners(owners)