from database.connection import get_connection

from models.user import User


class UserRepository:

    def get_by_username(
            self,
            username
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

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

        finally:

            cursor.close()
            connection.close()

    def get_by_email(
            self,
            email
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

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
                WHERE email = ?
                """,
                (
                    email,
                )
            )

            row = cursor.fetchone()

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

        finally:

            cursor.close()
            connection.close()

    def update_password(
            self,
            user_id,
            password_hash
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            UPDATE Users
            SET password_hash = ?
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    password_hash,
                    user_id
                )
            )

            connection.commit()

        finally:

            cursor.close()
            connection.close()