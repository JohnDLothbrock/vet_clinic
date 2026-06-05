import pytest

from models.appointments import Appointment

from services.appointment_service import (
    AppointmentService
)

from exceptions.pet_not_found_exception import (
    PetNotFoundException
)


class FakeRepository:

    def create(self, appointment):
        pass


class TrackingRepository:

    def __init__(self):
        self.was_called = False

    def create(self, appointment):
        self.was_called = True


class InvalidPetService:

    def get_pet_by_id(
        self,
        pet_id
    ):
        return None


class ValidPetService:

    def get_pet_by_id(
        self,
        pet_id
    ):
        return {
            "id": pet_id
        }


def test_create_appointment_invalid_pet():

    service = AppointmentService(
        FakeRepository(),
        InvalidPetService()
    )

    appointment = Appointment(
        999,
        "2099-01-01 10:00",
        "Checkup"
    )

    with pytest.raises(
        PetNotFoundException
    ):
        service.create_appointment(
            appointment
        )


def test_create_appointment_success():

    repository = (
        TrackingRepository()
    )

    service = AppointmentService(
        repository,
        ValidPetService()
    )

    appointment = Appointment(
        1,
        "2099-01-01 10:00",
        "Checkup"
    )

    service.create_appointment(
        appointment
    )

    assert repository.was_called