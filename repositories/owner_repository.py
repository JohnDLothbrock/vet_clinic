from math import ceil

from database.connection import get_connection
from models.owner import Owner


class OwnerRepository:

    def create(self, owner):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            INSERT INTO Owners (
                name,
                phone
            )
            OUTPUT INSERTED.id
            VALUES (?, ?)
            """

            cursor.execute(
                query,
                (
                    owner.name,
                    owner.phone
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
                name,
                phone
            FROM Owners
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            owners = []

            for row in rows:

                owner = Owner(
                    name=row.name,
                    phone=row.phone,
                    owner_id=row.id
                )

                owners.append(owner)

            return owners

        finally:

            cursor.close()
            connection.close()

    def get_by_id(self, owner_id):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                name,
                phone
            FROM Owners
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    owner_id,
                )
            )

            row = cursor.fetchone()

            if row:

                return Owner(
                    name=row.name,
                    phone=row.phone,
                    owner_id=row.id
                )

            return None

        finally:

            cursor.close()
            connection.close()

    def update(self, owner):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            UPDATE Owners
            SET
                name = ?,
                phone = ?
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    owner.name,
                    owner.phone,
                    owner.id
                )
            )

            connection.commit()

        finally:

            cursor.close()
            connection.close()

    def delete(self, owner_id):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            DELETE FROM Owners
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    owner_id,
                )
            )

            connection.commit()

        finally:

            cursor.close()
            connection.close()

    def get_by_name(
            self,
            name
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                name,
                phone
            FROM Owners
            WHERE name LIKE ?
            """

            cursor.execute(
                query,
                (
                    f"%{name}%",
                )
            )

            rows = cursor.fetchall()

            owners = []

            for row in rows:

                owner = Owner(
                    name=row.name,
                    phone=row.phone,
                    owner_id=row.id
                )

                owners.append(owner)

            return owners

        finally:

            cursor.close()
            connection.close()

    def get_paginated(
            self,
            page: int,
            page_size: int,
            search: str | None = None
    ):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            where_sql = ""
            params = []

            if search:

                where_sql = """
                WHERE
                    name LIKE ?
                    OR phone LIKE ?
                """

                search_value = f"%{search}%"

                params.extend(
                    [
                        search_value,
                        search_value
                    ]
                )

            count_query = f"""
            SELECT
                COUNT(*) AS total
            FROM Owners
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
                name,
                phone
            FROM Owners
            {where_sql}
            ORDER BY id DESC
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

            owners = []

            for row in rows:

                owners.append(
                    {
                        "id": row.id,
                        "name": row.name,
                        "phone": row.phone
                    }
                )

            total_pages = (
                ceil(total / page_size)
                if total > 0
                else 0
            )

            return {
                "items": owners,
                "total": total,
                "page": page,
                "page_size": page_size,
                "total_pages": total_pages
            }

        finally:

            cursor.close()
            connection.close()