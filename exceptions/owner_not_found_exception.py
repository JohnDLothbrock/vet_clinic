from exceptions.not_found_exception import (
    NotFoundException
)


class OwnerNotFoundException(
    NotFoundException
):

    def __init__(
        self,
        owner_id
    ):

        super().__init__(
            f"Owner with ID {owner_id} does not exist."
        )