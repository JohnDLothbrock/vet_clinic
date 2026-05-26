from exceptions.validation_exception import (
    ValidationException
)


class OwnerValidator:

    @staticmethod
    def validate(
        name,
        phone
    ):

        if not name.strip():

            raise ValidationException(
                "Owner name cannot be empty."
            )

        if len(name.strip()) < 2:

            raise ValidationException(
                "Owner name is too short."
            )

        if not phone.strip():

            raise ValidationException(
                "Phone cannot be empty."
            )