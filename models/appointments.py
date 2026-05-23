class Appointment:

    def __init__(
            self,
            pet_id,
            appointment_date,
            reason,
            appointment_id=None
    ):

        self.id = appointment_id
        self.pet_id = pet_id
        self.appointment_date = appointment_date
        self.reason = reason