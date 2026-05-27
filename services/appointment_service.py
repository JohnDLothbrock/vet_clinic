from exceptions.pet_not_found_exception import (
    PetNotFoundException
)
from exceptions.appointment_not_found_exception import (
    AppointmentNotFoundException
)
from utils.logger import logger
from validators.appointment_validator import (
    AppointmentValidator
)


class AppointmentService:


    def __init__(
            self,
            appointment_repository,
            pet_service
    ):

        self.appointment_repository = (
            appointment_repository
        )

        self.pet_service = (
            pet_service
        )


    def create_appointment(
            self,
            appointment
    ):

        pet = (
            self.pet_service.get_pet_by_id(
                appointment.pet_id
            )
        )

        if not pet:

            logger.warning(
                f"Pet ID {appointment.pet_id} not found"
            )

            raise PetNotFoundException(
                appointment.pet_id
            )

        AppointmentValidator.validate(
            appointment.appointment_date,
            appointment.reason
        )

        self.appointment_repository.create(
            appointment
        )

        logger.info(
            f"Appointment created for pet {appointment.pet_id}"
        )


    def get_all_appointments(
            self
    ):

        return (
            self.appointment_repository.get_all()
        )


    def get_appointment_by_id(
            self,
            appointment_id
    ):

        appointment = (
            self.appointment_repository.get_by_id(
                appointment_id
            )
        )

        if not appointment:
            logger.warning(
                f"Appointment ID {appointment_id} not found"
            )

            raise AppointmentNotFoundException(
                appointment_id
            )
        return appointment


    def update_appointment(
            self,
            appointment_id,
            appointment_date,
            reason
    ):

        appointment = (
            self.appointment_repository.get_by_id(
                appointment_id
            )
        )

        if not appointment:

            logger.warning(
                f"Appointment ID {appointment_id} not found"
            )

            raise AppointmentNotFoundException(
                appointment_id
            )

        appointment.appointment_date = (
            appointment_date
        )

        appointment.reason = reason

        AppointmentValidator.validate(
            appointment_date,
            reason
        )

        self.appointment_repository.update(
            appointment
        )

        logger.info(
            f"Appointment updated: {appointment_id}"
        )


    def delete_appointment(
            self,
            appointment_id
    ):

        appointment = (
            self.appointment_repository.get_by_id(
                appointment_id
            )
        )

        if not appointment:

            logger.warning(
                f"Appointment ID {appointment_id} not found"
            )

            raise AppointmentNotFoundException(
                appointment_id
            )

        self.appointment_repository.delete(
            appointment_id
        )

        logger.info(
            f"Appointment deleted: {appointment_id}"
        )


    def search_appointments_by_pet_id(
            self,
            pet_id
    ):

        logger.info(
            f"Searching appointments for pet ID: {pet_id}"
        )

        return (
            self.appointment_repository.get_by_pet_id(
                pet_id
            )
        )