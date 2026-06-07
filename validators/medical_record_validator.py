from exceptions.validation_exception import (
    ValidationException
)

from datetime import datetime


class MedicalRecordValidator:

    @staticmethod
    def validate(
            visit_date,
            weight,
            diagnosis,
            treatment
    ):

        if not diagnosis.strip():

            raise ValidationException(
                "Diagnosis cannot be empty."
            )

        if not treatment.strip():

            raise ValidationException(
                "Treatment cannot be empty."
            )

        if weight <= 0:

            raise ValidationException(
                "Weight must be greater than zero."
            )

        try:

            datetime.strptime(
                visit_date,
                "%Y-%m-%d %H:%M"
            )

        except ValueError:

            raise ValidationException(
                "Date format must be YYYY-MM-DD HH:MM"
            )