from models.owner import Owner
from services.owner_service import OwnerService
from views.owner_view import OwnerView
from exceptions.owner_not_found_exception import OwnerNotFoundException
from repositories.owner_repository import (
    OwnerRepository
)


class OwnerController:

    def __init__(
            self,
            owner_service
    ):

        self.owner_service = owner_service
        self.owner_view = OwnerView()

    def create_owner(self):

        name, phone = self.owner_view.get_owner_data()
        owner = Owner(name, phone)
        self.owner_service.create_owner(owner)

    def show_owners(self):

        owners = self.owner_service.get_all_owners()
        self.owner_view.display_owners(owners)

    def update_owner(self):

        try:
            owner_id, name, phone = self.owner_view.get_owner_update_data()
            self.owner_service.update_owner(owner_id, name, phone)
            print("Owner updated successfully.")

        except OwnerNotFoundException as error:
            print(error)

    def delete_owner(self):
        try:

            owner_id = self.owner_view.get_owner_id()

            self.owner_service.delete_owner(owner_id)

            print("Owner deleted successfully.")

        except OwnerNotFoundException as error:

            print(error)