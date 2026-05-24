from exceptions.pet_not_found_exception import (
    PetNotFoundException
)
from exceptions.appointment_not_found_exception import (
    AppointmentNotFoundException
)



class AppointmentService:


    def __init__(self, appointment_repository, pet_service):
        self.appointment_repository = appointment_repository
        self.pet_service = pet_service


    def create_appointment(self, appointment):

        pet = self.pet_service.get_pet_by_id(appointment.pet_id)

        if not pet:
            raise PetNotFoundException(
                appointment.pet_id
            )

        self.appointment_repository.create(appointment)


    def get_all_appointments(self):
        return self.appointment_repository.get_all()


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
            raise AppointmentNotFoundException(
                appointment_id
            )

        appointment.appointment_date = (
            appointment_date
        )

        appointment.reason = reason

        self.appointment_repository.update(
            appointment
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
            raise AppointmentNotFoundException(
                appointment_id
            )

        self.appointment_repository.delete(
            appointment_id
        )


    