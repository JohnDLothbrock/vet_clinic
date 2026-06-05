import pytest

from datetime import (
    datetime,
    timedelta
)

from validators.appointment_validator import (
    AppointmentValidator
)

from exceptions.validation_exception import (
    ValidationException
)


def test_valid_appointment():

    future_date = (
        datetime.now()
        + timedelta(days=1)
    ).strftime(
        "%Y-%m-%d %H:%M"
    )

    AppointmentValidator.validate(
        future_date,
        "Vaccination"
    )


def test_empty_reason():

    future_date = (
        datetime.now()
        + timedelta(days=1)
    ).strftime(
        "%Y-%m-%d %H:%M"
    )

    with pytest.raises(
        ValidationException
    ):
        AppointmentValidator.validate(
            future_date,
            ""
        )


def test_invalid_date_format():

    with pytest.raises(
        ValidationException
    ):
        AppointmentValidator.validate(
            "01/01/2025",
            "Checkup"
        )