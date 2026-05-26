from datetime import datetime

from exceptions.validation_exception import (
    ValidationException
)


class AppointmentValidator:

    @staticmethod
    def validate(
        appointment_date,
        reason
    ):

        if not reason.strip():

            raise ValidationException(
                "Reason cannot be empty."
            )

        try:

            datetime.strptime(
                appointment_date,
                "%Y-%m-%d %H:%M"
            )

        except ValueError:

            raise ValidationException(
                "Date format must be YYYY-MM-DD HH:MM"
            )
    