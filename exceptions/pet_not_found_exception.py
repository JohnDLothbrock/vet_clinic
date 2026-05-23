class PetNotFoundException(Exception):

    def __init__(
        self,
        pet_id: int
    ):

        super().__init__(
            f"Pet with ID {pet_id} was not found."
        )
