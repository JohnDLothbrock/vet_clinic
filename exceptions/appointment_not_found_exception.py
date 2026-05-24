class AppointmentNotFoundException(
    Exception
):

    def __init__(
        self,
        appointment_id
    ):

        super().__init__(
            f"Appointment with ID "
            f"{appointment_id} does not exist."
        )

