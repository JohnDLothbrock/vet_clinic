import pytest

from validators.owner_validator import (
    OwnerValidator
)

from exceptions.validation_exception import (
    ValidationException
)


def test_valid_owner():

    OwnerValidator.validate(
        "Juan",
        "88888888"
    )


def test_empty_name():

    with pytest.raises(
        ValidationException
    ):
        OwnerValidator.validate(
            "",
            "88888888"
        )


def test_short_name():

    with pytest.raises(
        ValidationException
    ):
        OwnerValidator.validate(
            "J",
            "88888888"
        )


def test_empty_phone():

    with pytest.raises(
        ValidationException
    ):
        OwnerValidator.validate(
            "Juan",
            ""
        )


def test_invalid_phone():

    with pytest.raises(
        ValidationException
    ):
        OwnerValidator.validate(
            "Juan",
            "abc"
        )