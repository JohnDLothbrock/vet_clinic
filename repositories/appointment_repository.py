from math import ceil

from database.connection import get_connection

from models.appointments import Appointment


class AppointmentRepository:

    def get_recent_appointments(
            self,
            limit=5
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = f"""
            SELECT TOP {limit}
                a.id,
                a.pet_id,
                p.name AS pet_name,
                a.appointment_date,
                a.reason
            FROM Appointments a
            INNER JOIN Pets p
                ON a.pet_id = p.id
            ORDER BY a.appointment_date DESC
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            appointments = []

            for row in rows:

                appointments.append(
                    {
                        "id": row.id,
                        "pet_id": row.pet_id,
                        "pet_name": row.pet_name,
                        "appointment_date": row.appointment_date,
                        "reason": row.reason
                    }
                )

            return appointments

        finally:

            cursor.close()
            connection.close()

    def create(
            self,
            appointment
    ) -> int:

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            INSERT INTO Appointments (
                pet_id,
                appointment_date,
                reason
            )
            OUTPUT INSERTED.id
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

            row = cursor.fetchone()

            connection.commit()

            return row[0]

        finally:

            cursor.close()
            connection.close()

    def get_all(self):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                pet_id,
                appointment_date,
                reason
            FROM Appointments
            """

            cursor.execute(query)

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

    def get_by_id(
            self,
            appointment_id
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                pet_id,
                appointment_date,
                reason
            FROM Appointments
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    appointment_id,
                )
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

    def update(
            self,
            appointment
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            UPDATE Appointments
            SET
                appointment_date = ?,
                reason = ?
            WHERE id = ?
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

        finally:

            cursor.close()
            connection.close()

    def delete(
            self,
            appointment_id
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            DELETE FROM Appointments
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    appointment_id,
                )
            )

            connection.commit()

        finally:

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
            SELECT
                a.id,
                a.pet_id,
                p.name AS pet_name,
                a.appointment_date,
                a.reason
            FROM Appointments a
            INNER JOIN Pets p
                ON a.pet_id = p.id
            WHERE a.pet_id = ?
            ORDER BY a.appointment_date DESC
            """

            cursor.execute(
                query,
                (
                    pet_id,
                )
            )

            rows = cursor.fetchall()

            appointments = []

            for row in rows:

                appointments.append(
                    {
                        "id": row.id,
                        "pet_id": row.pet_id,
                        "pet_name": row.pet_name,
                        "appointment_date": row.appointment_date,
                        "reason": row.reason
                    }
                )

            return appointments

        finally:

            cursor.close()
            connection.close()

    def get_all_with_pet(self):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                a.id,
                a.pet_id,
                p.name AS pet_name,
                a.appointment_date,
                a.reason
            FROM Appointments a
            INNER JOIN Pets p
                ON a.pet_id = p.id
            ORDER BY a.appointment_date DESC
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            appointments = []

            for row in rows:

                appointments.append(
                    {
                        "id": row.id,
                        "pet_id": row.pet_id,
                        "pet_name": row.pet_name,
                        "appointment_date": row.appointment_date,
                        "reason": row.reason
                    }
                )

            return appointments

        finally:

            cursor.close()
            connection.close()

    def get_paginated_with_pet(
            self,
            page: int,
            page_size: int,
            search: str | None = None,
            pet_id: int | None = None,
            date_from: str | None = None,
            date_to: str | None = None
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            where_clauses = []
            params = []

            if search:

                where_clauses.append(
                    """
                    (
                        a.reason LIKE ?
                        OR p.name LIKE ?
                    )
                    """
                )

                search_value = f"%{search}%"

                params.extend(
                    [
                        search_value,
                        search_value
                    ]
                )

            if pet_id:

                where_clauses.append(
                    "a.pet_id = ?"
                )

                params.append(
                    pet_id
                )

            if date_from:

                where_clauses.append(
                    "a.appointment_date >= ?"
                )

                params.append(
                    date_from
                )

            if date_to:

                where_clauses.append(
                    "a.appointment_date <= ?"
                )

                params.append(
                    date_to
                )

            where_sql = ""

            if where_clauses:

                where_sql = (
                    "WHERE " +
                    " AND ".join(
                        where_clauses
                    )
                )

            count_query = f"""
            SELECT
                COUNT(*) AS total
            FROM Appointments a
            INNER JOIN Pets p
                ON a.pet_id = p.id
            {where_sql}
            """

            cursor.execute(
                count_query,
                tuple(params)
            )

            total_row = cursor.fetchone()

            total = (
                total_row[0]
                if total_row
                else 0
            )

            offset = (
                page - 1
            ) * page_size

            data_query = f"""
            SELECT
                a.id,
                a.pet_id,
                p.name AS pet_name,
                a.appointment_date,
                a.reason
            FROM Appointments a
            INNER JOIN Pets p
                ON a.pet_id = p.id
            {where_sql}
            ORDER BY a.appointment_date DESC
            OFFSET ? ROWS
            FETCH NEXT ? ROWS ONLY
            """

            data_params = (
                params +
                [
                    offset,
                    page_size
                ]
            )

            cursor.execute(
                data_query,
                tuple(data_params)
            )

            rows = cursor.fetchall()

            appointments = []

            for row in rows:

                appointments.append(
                    {
                        "id": row.id,
                        "pet_id": row.pet_id,
                        "pet_name": row.pet_name,
                        "appointment_date": row.appointment_date,
                        "reason": row.reason
                    }
                )

            total_pages = (
                ceil(total / page_size)
                if total > 0
                else 0
            )

            return {
                "items": appointments,
                "total": total,
                "page": page,
                "page_size": page_size,
                "total_pages": total_pages
            }

        finally:

            cursor.close()
            connection.close()