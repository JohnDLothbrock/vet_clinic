from database.connection import get_connection


class AppointmentRepository:

    def create(self, appointment):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO Appointments (
            pet_id,
            appointment_date,
            reason
        )
        VALUES (?, ?, ?)
        """

        cursor.execute(
            query,
            (
                appointment.pet_id,
                appointment.appointment_date,
                appointment.reason
            )
        )

        connection.commit()

        cursor.close()
        connection.close()

    def get_all(self):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT *
        FROM Appointments
        """

        cursor.execute(query)

        appointments = cursor.fetchall()

        cursor.close()
        connection.close()

        return appointments