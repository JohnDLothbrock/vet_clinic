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

        if not phone.isdigit():
            raise ValidationException(
                "Phone must contain only numbers."
            )
        if len(phone) < 8:
            raise ValidationException(
                "Phone must contain at least 8 digits."
            )
        if len(phone) > 15:
            raise ValidationException(
                "Phone must not contain more than 15 digits."
            )