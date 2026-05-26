from exceptions.not_found_exception import (
    NotFoundException
)


class AppointmentNotFoundException(
    NotFoundException
):

    def __init__(
        self,
        appointment_id
    ):

        super().__init__(
            f"Appointment with ID {appointment_id} does not exist."
        )