from exceptions.validation_exception import (
    ValidationException
)


class PetValidator:

    @staticmethod
    def validate(
        name,
        species,
        age
    ):

        if not name.strip():

            raise ValidationException(
                "Pet name cannot be empty."
            )

        if not species.strip():

            raise ValidationException(
                "Species cannot be empty."
            )

        if age < 0:

            raise ValidationException(
                "Age cannot be negative."
            )
    