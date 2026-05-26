from exceptions.not_found_exception import (
    NotFoundException
)


class PetNotFoundException(
    NotFoundException
):

    def __init__(
        self,
        pet_id
    ):

        super().__init__(
            f"Pet with ID {pet_id} does not exist."
        )