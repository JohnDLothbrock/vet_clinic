from exceptions.application_exception import (
    ApplicationException
)


class AppointmentNotFoundException(
    ApplicationException
):

    def __init__(
        self,
        appointment_id
    ):

        super().__init__(
            f"Appointment with ID {appointment_id} does not exist."
        )