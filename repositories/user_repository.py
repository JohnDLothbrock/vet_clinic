from database.connection import get_connection

from models.user import User


class UserRepository:

    def get_by_username(
            self,
            username
    ):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                username,
                email,
                password_hash,
                role_id,
                active
            FROM Users
            WHERE username = ?
            """,
            (
                username,
            )
        )

        row = cursor.fetchone()

        connection.close()

        if not row:

            return None

        return User(
            user_id=row.id,
            username=row.username,
            email=row.email,
            password_hash=row.password_hash,
            role_id=row.role_id,
            active=row.active
        )