
class AppointmentService:

    def __init__(
        self,
        appointment_repository
    ):

        self.appointment_repository = (
            appointment_repository
        )

    def create_appointment(self, appointment):

        self.appointment_repository.create(
            appointment
        )

    def get_all_appointments(self):

        return (
            self.appointment_repository.get_all()
        )