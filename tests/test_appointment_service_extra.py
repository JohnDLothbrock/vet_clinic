import pytest

from services.appointment_service import (
    AppointmentService
)

from models.appointments import Appointment

from exceptions.appointment_not_found_exception import (
    AppointmentNotFoundException
)


class ValidPetService:

    def get_pet_by_id(
        self,
        pet_id
    ):
        return {
            "id": pet_id
        }


def test_get_appointment_by_id_success():

    class Repo:

        def get_by_id(
            self,
            appointment_id
        ):
            return Appointment(
                1,
                "2099-01-01 10:00",
                "Checkup",
                appointment_id
            )

    service = AppointmentService(
        Repo(),
        ValidPetService()
    )

    appointment = (
        service.get_appointment_by_id(
            1
        )
    )

    assert appointment.id == 1


def test_get_appointment_by_id_not_found():

    class Repo:

        def get_by_id(
            self,
            appointment_id
        ):
            return None

    service = AppointmentService(
        Repo(),
        ValidPetService()
    )

    with pytest.raises(
        AppointmentNotFoundException
    ):
        service.get_appointment_by_id(
            999
        )