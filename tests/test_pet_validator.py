import pytest

from validators.pet_validator import (
    PetValidator
)

from exceptions.validation_exception import (
    ValidationException
)


def test_valid_pet():

    PetValidator.validate(
        "Max",
        "Dog",
        3
    )


def test_empty_name():

    with pytest.raises(
        ValidationException
    ):
        PetValidator.validate(
            "",
            "Dog",
            3
        )


def test_empty_species():

    with pytest.raises(
        ValidationException
    ):
        PetValidator.validate(
            "Max",
            "",
            3
        )


def test_invalid_age():

    with pytest.raises(
        ValidationException
    ):
        PetValidator.validate(
            "Max",
            "Dog",
            0
        )