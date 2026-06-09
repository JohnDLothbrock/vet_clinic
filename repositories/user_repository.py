from database.connection import get_connection

from models.user import User


class UserRepository:

    def create(
            self,
            user: User
    ) -> int:

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            INSERT INTO Users (
                username,
                email,
                password_hash,
                role_id,
                active,
                created_at
            )
            OUTPUT INSERTED.id
            VALUES (?, ?, ?, ?, 1, SYSDATETIME())
            """

            cursor.execute(
                query,
                (
                    user.username,
                    user.email,
                    user.password_hash,
                    user.role_id
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
                username,
                email,
                password_hash,
                role_id,
                active
            FROM Users
            ORDER BY id
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            users = []

            for row in rows:

                users.append(
                    User(
                        user_id=row.id,
                        username=row.username,
                        email=row.email,
                        password_hash=row.password_hash,
                        role_id=row.role_id,
                        active=row.active
                    )
                )

            return users

        finally:

            cursor.close()
            connection.close()

    def get_by_id(
            self,
            user_id
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                username,
                email,
                password_hash,
                role_id,
                active
            FROM Users
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    user_id,
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

    def update_role(
            self,
            user_id,
            role_id
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            UPDATE Users
            SET role_id = ?
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    role_id,
                    user_id
                )
            )

            connection.commit()

        finally:

            cursor.close()
            connection.close()

    def update_active(
            self,
            user_id,
            active
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            UPDATE Users
            SET active = ?
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    active,
                    user_id
                )
            )

            connection.commit()

        finally:

            cursor.close()
            connection.close()