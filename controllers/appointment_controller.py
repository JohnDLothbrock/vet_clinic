from models.appointments import Appointment
from services.appointment_service import AppointmentService
from views.appointment_view import AppointmentView
from repositories.appointment_repository import (
    AppointmentRepository
)


class AppointmentController:

    def __init__(self):
        appointment_repository = (
            AppointmentRepository()
        )
        self.appointment_service = (
            AppointmentService(
                appointment_repository
            )
        )
        self.appointment_view = AppointmentView()

    def create_appointment(self):
        (
            pet_id,
            appointment_date,
            reason

        ) = self.appointment_view.get_appointment_data()
        
        appointment = Appointment(
            pet_id,
            appointment_date,
            reason
        )
        self.appointment_service.create_appointment(
            appointment
        )

    def show_appointments(self):
        appointments = (
            self.appointment_service.get_all_appointments()
        )
        self.appointment_view.display_appointments(
            appointments
        )