from exceptions.application_exception import (
    ApplicationException
)


class PetNotFoundException(
    ApplicationException
):

    def __init__(
        self,
        pet_id
    ):

        super().__init__(
            f"Pet with ID {pet_id} does not exist."
        )