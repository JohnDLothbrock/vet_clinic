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
            pet_service,
            audit_log_service=None
    ):

        self.appointment_repository = (
            appointment_repository
        )

        self.pet_service = (
            pet_service
        )

        self.audit_log_service = (
            audit_log_service
        )

    def create_appointment(
            self,
            appointment,
            user_id=None
    ) -> int:

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

        appointment_id = (
            self.appointment_repository.create(
                appointment
            )
        )

        if self.audit_log_service and user_id:

            self.audit_log_service.create_audit_log(
                user_id=user_id,
                action="CREATE",
                entity="Appointment",
                entity_id=appointment_id
            )

        logger.info(
            (
                f"Appointment created: "
                f"{appointment_id} "
                f"for pet {appointment.pet_id}"
            )
        )

        return appointment_id

    def get_all_appointments(
            self
    ):

        return (
            self.appointment_repository.get_all()
        )

    def get_paginated_appointments_with_pet(
            self,
            page: int,
            page_size: int,
            search: str | None = None,
            pet_id: int | None = None,
            date_from: str | None = None,
            date_to: str | None = None
    ):

        logger.info(
            "Fetching paginated appointments with pet data"
        )

        if page < 1:

            page = 1

        if page_size < 1:

            page_size = 10

        if page_size > 100:

            page_size = 100

        return (
            self.appointment_repository
            .get_paginated_with_pet(
                page=page,
                page_size=page_size,
                search=search,
                pet_id=pet_id,
                date_from=date_from,
                date_to=date_to
            )
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
            reason,
            user_id=None
    ) -> int:

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

        if self.audit_log_service and user_id:

            self.audit_log_service.create_audit_log(
                user_id=user_id,
                action="UPDATE",
                entity="Appointment",
                entity_id=appointment_id
            )

        logger.info(
            f"Appointment updated: {appointment_id}"
        )

        return appointment_id

    def delete_appointment(
            self,
            appointment_id,
            user_id=None
    ) -> int:

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

        if self.audit_log_service and user_id:

            self.audit_log_service.create_audit_log(
                user_id=user_id,
                action="DELETE",
                entity="Appointment",
                entity_id=appointment_id
            )

        logger.info(
            f"Appointment deleted: {appointment_id}"
        )

        return appointment_id

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

    def get_all_appointments_with_pet(self):

        return (
            self.appointment_repository
            .get_all_with_pet()
        )