class OwnerNotFoundException(Exception):

    def __init__(self, owner_id):

        self.owner_id = owner_id

        super().__init__(
            f"Owner with ID {owner_id} does not exist."
        )