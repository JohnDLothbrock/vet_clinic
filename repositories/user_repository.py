from math import ceil

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

    def get_paginated(
            self,
            page: int,
            page_size: int,
            search: str | None = None,
            role_id: int | None = None,
            active: bool | None = None
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
                        username LIKE ?
                        OR email LIKE ?
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

            if role_id:

                where_clauses.append(
                    "role_id = ?"
                )

                params.append(
                    role_id
                )

            if active is not None:

                where_clauses.append(
                    "active = ?"
                )

                params.append(
                    active
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
            FROM Users
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
                id,
                username,
                email,
                password_hash,
                role_id,
                active
            FROM Users
            {where_sql}
            ORDER BY id
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

            users = []

            for row in rows:

                users.append(
                    {
                        "id": row.id,
                        "username": row.username,
                        "email": row.email,
                        "role_id": row.role_id,
                        "active": bool(row.active)
                    }
                )

            total_pages = (
                ceil(total / page_size)
                if total > 0
                else 0
            )

            return {
                "items": users,
                "total": total,
                "page": page,
                "page_size": page_size,
                "total_pages": total_pages
            }

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