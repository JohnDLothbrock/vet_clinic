from exceptions.application_exception import (
    ApplicationException
)


class OwnerNotFoundException(
    ApplicationException
):

    def __init__(
            self,
            owner_id: int
    ):

        super().__init__(
            f"Owner with ID {owner_id} not found",
            404
        )