from models.appointments import Appointment
from services.appointment_service import AppointmentService
from views.appointment_view import AppointmentView
from exceptions.pet_not_found_exception import (
    PetNotFoundException
)
from repositories.appointment_repository import (
    AppointmentRepository
)
from repositories.pet_repository import PetRepository
from services.pet_service import PetService
from exceptions.appointment_not_found_exception import (
    AppointmentNotFoundException
)
from repositories.owner_repository import (
    OwnerRepository
)
from services.owner_service import (
    OwnerService
)


class AppointmentController:

    def __init__(
            self,
            appointment_service
    ):

        self.appointment_service = (
            appointment_service
        )

        self.appointment_view = (
            AppointmentView()
        )


    def create_appointment(self):
        try:
            pet_id, appointment_date, reason = (
                self.appointment_view.get_appointment_data()
            )
            appointment = Appointment(
                pet_id,
                appointment_date,
                reason
            )

            self.appointment_service.create_appointment(appointment)
            print("Appointment created successfully.")


        except PetNotFoundException as error:
            print(error)


    def show_appointments(self):
        appointments = (
            self.appointment_service.get_all_appointments()
        )
        self.appointment_view.display_appointments(
            appointments
        )


    def update_appointment(self):
        try:

            (
                appointment_id,
                appointment_date,
                reason
            ) = (
                self.appointment_view
                .get_appointment_update_data()
            )

            self.appointment_service.update_appointment(
                appointment_id,
                appointment_date,
                reason
            )

            print(
                "Appointment updated successfully."
            )

        except AppointmentNotFoundException as error:

            print(error)


    def delete_appointment(self):
        try:

            appointment_id = (
                self.appointment_view
                .get_appointment_id()
            )

            self.appointment_service.delete_appointment(
                appointment_id
            )
            print(
                "Appointment deleted successfully."
            )

        except AppointmentNotFoundException as error:
            print(error)