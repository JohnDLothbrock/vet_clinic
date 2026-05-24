class AppointmentView:

    def get_appointment_data(self):

        pet_id = int(input("Pet ID: "))

        appointment_date = input(
            "Appointment Date (YYYY-MM-DD HH:MM): "
        )

        reason = input("Reason: ")

        return (
            pet_id,
            appointment_date,
            reason
        )

    def display_appointments(self, appointments):

        print("\n--- APPOINTMENTS ---")

        for appointment in appointments:

            print(f"""
ID: {appointment.id}
Pet ID: {appointment.pet_id}
Date: {appointment.appointment_date}
Reason: {appointment.reason}
            """)


    def get_appointment_update_data(self):
        appointment_id = int(
            input("Appointment ID: ")
        )

        appointment_date = input(
            "New date (YYYY-MM-DD HH:MM): "
        )

        reason = input(
            "New reason: "
        )

        return (
            appointment_id,
            appointment_date,
            reason
        )


    def get_appointment_id(self):
        return int(
            input("Appointment ID: ")
        )