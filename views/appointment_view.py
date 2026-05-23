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

