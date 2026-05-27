from database.connection import get_connection
from models.appointments import Appointment


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
                SELECT id, pet_id, appointment_date, reason
                FROM Appointments \
                """

        cursor.execute(query)
        rows = cursor.fetchall()

        appointments = []

        for row in rows:
            appointment = Appointment(
                pet_id=row[1],
                appointment_date=row[2],
                reason=row[3],
                appointment_id=row[0]
            )

            appointments.append(appointment)

        cursor.close()
        connection.close()

        return appointments

    def get_by_id(self, appointment_id):

        connection = get_connection()
        cursor = connection.cursor()

        try:
            query = """
                    SELECT id, \
                           pet_id, \
                           appointment_date, \
                           reason
                    FROM Appointments
                    WHERE id = ? \
                    """

            cursor.execute(
                query,
                (appointment_id,)
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return Appointment(
                pet_id=row.pet_id,
                appointment_date=row.appointment_date,
                reason=row.reason,
                appointment_id=row.id
            )

        finally:
            cursor.close()
            connection.close()


    def update(self, appointment):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
                UPDATE Appointments
                SET appointment_date = ?,
                    reason           = ?
                WHERE id = ? \
                """

        cursor.execute(
            query,
            (
                appointment.appointment_date,
                appointment.reason,
                appointment.id
            )
        )

        connection.commit()

        cursor.close()
        connection.close()

    def delete(self, appointment_id):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
                DELETE \
                FROM Appointments
                WHERE id = ? \
                """

        cursor.execute(
            query,
            (appointment_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()


    def get_by_pet_id(
            self,
            pet_id
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:
            query = """
                    SELECT id, \
                           pet_id, \
                           appointment_date, \
                           reason
                    FROM Appointments
                    WHERE pet_id = ? \
                    """

            cursor.execute(
                query,
                (pet_id,)
            )

            rows = cursor.fetchall()
            appointments = []

            for row in rows:
                appointment = Appointment(
                    pet_id=row.pet_id,
                    appointment_date=row.appointment_date,
                    reason=row.reason,
                    appointment_id=row.id
                )

                appointments.append(
                    appointment
                )
            return appointments

        finally:
            cursor.close()
            connection.close()