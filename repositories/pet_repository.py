from math import ceil

from models.pet import Pet

from repositories.base_repository import (
    BaseRepository
)


class PetRepository(
    BaseRepository
):

    def create(
            self,
            pet: Pet
    ) -> int:

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            INSERT INTO Pets (
                name,
                species,
                age,
                owner_id
            )
            OUTPUT INSERTED.id
            VALUES (?, ?, ?, ?)
            """

            cursor.execute(
                query,
                (
                    pet.name,
                    pet.species,
                    pet.age,
                    pet.owner_id
                )
            )

            row = cursor.fetchone()

            connection.commit()

            return row[0]

        finally:

            self._close(
                connection,
                cursor
            )

    def get_all(
            self
    ) -> list[Pet]:

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                name,
                species,
                age,
                owner_id
            FROM Pets
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            pets = []

            for row in rows:

                pets.append(
                    Pet(
                        name=row.name,
                        species=row.species,
                        age=row.age,
                        owner_id=row.owner_id,
                        pet_id=row.id
                    )
                )

            return pets

        finally:

            self._close(
                connection,
                cursor
            )

    def get_by_id(
            self,
            pet_id: int
    ) -> Pet | None:

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                name,
                species,
                age,
                owner_id
            FROM Pets
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    pet_id,
                )
            )

            row = cursor.fetchone()

            if row is None:

                return None

            return Pet(
                name=row.name,
                species=row.species,
                age=row.age,
                owner_id=row.owner_id,
                pet_id=row.id
            )

        finally:

            self._close(
                connection,
                cursor
            )

    def update(
            self,
            pet_id,
            name,
            species,
            age
    ):

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            UPDATE Pets
            SET
                name = ?,
                species = ?,
                age = ?
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    name,
                    species,
                    age,
                    pet_id
                )
            )

            connection.commit()

        finally:

            self._close(
                connection,
                cursor
            )

    def delete(
            self,
            pet_id
    ):

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            DELETE FROM Pets
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    pet_id,
                )
            )

            connection.commit()

        finally:

            self._close(
                connection,
                cursor
            )

    def get_by_name(
            self,
            name
    ) -> list[Pet]:

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                name,
                species,
                age,
                owner_id
            FROM Pets
            WHERE name LIKE ?
            """

            cursor.execute(
                query,
                (
                    f"%{name}%",
                )
            )

            rows = cursor.fetchall()

            pets = []

            for row in rows:

                pets.append(
                    Pet(
                        name=row.name,
                        species=row.species,
                        age=row.age,
                        owner_id=row.owner_id,
                        pet_id=row.id
                    )
                )

            return pets

        finally:

            self._close(
                connection,
                cursor
            )

    def get_by_name_with_owner(
            self,
            name
    ):

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                p.id,
                p.name,
                p.species,
                p.age,
                p.owner_id,
                o.name AS owner_name
            FROM Pets p
            INNER JOIN Owners o
                ON p.owner_id = o.id
            WHERE p.name LIKE ?
            """

            cursor.execute(
                query,
                (
                    f"%{name}%",
                )
            )

            rows = cursor.fetchall()

            pets = []

            for row in rows:

                pets.append(
                    {
                        "id": row.id,
                        "name": row.name,
                        "species": row.species,
                        "age": row.age,
                        "owner_id": row.owner_id,
                        "owner_name": row.owner_name
                    }
                )

            return pets

        finally:

            self._close(
                connection,
                cursor
            )

    def get_all_with_owner(self):

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                p.id,
                p.name,
                p.species,
                p.age,
                p.owner_id,
                o.name AS owner_name
            FROM Pets p
            INNER JOIN Owners o
                ON p.owner_id = o.id
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            pets = []

            for row in rows:

                pets.append(
                    {
                        "id": row.id,
                        "name": row.name,
                        "species": row.species,
                        "age": row.age,
                        "owner_id": row.owner_id,
                        "owner_name": row.owner_name
                    }
                )

            return pets

        finally:

            self._close(
                connection,
                cursor
            )

    def get_paginated_with_owner(
            self,
            page: int,
            page_size: int,
            search: str | None = None,
            species: str | None = None,
            owner_id: int | None = None
    ):

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            where_clauses = []
            params = []

            if search:

                where_clauses.append(
                    """
                    (
                        p.name LIKE ?
                        OR p.species LIKE ?
                        OR o.name LIKE ?
                    )
                    """
                )

                search_value = f"%{search}%"

                params.extend(
                    [
                        search_value,
                        search_value,
                        search_value
                    ]
                )

            if species:

                where_clauses.append(
                    "p.species LIKE ?"
                )

                params.append(
                    f"%{species}%"
                )

            if owner_id:

                where_clauses.append(
                    "p.owner_id = ?"
                )

                params.append(
                    owner_id
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
            FROM Pets p
            INNER JOIN Owners o
                ON p.owner_id = o.id
            {where_sql}
            """

            cursor.execute(
                count_query,
                tuple(params)
            )

            total_row = cursor.fetchone()

            total = (
                total_row.total
                if total_row
                else 0
            )

            offset = (
                page - 1
            ) * page_size

            data_query = f"""
            SELECT
                p.id,
                p.name,
                p.species,
                p.age,
                p.owner_id,
                o.name AS owner_name
            FROM Pets p
            INNER JOIN Owners o
                ON p.owner_id = o.id
            {where_sql}
            ORDER BY p.id DESC
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

            pets = []

            for row in rows:

                pets.append(
                    {
                        "id": row.id,
                        "name": row.name,
                        "species": row.species,
                        "age": row.age,
                        "owner_id": row.owner_id,
                        "owner_name": row.owner_name
                    }
                )

            total_pages = (
                ceil(total / page_size)
                if total > 0
                else 0
            )

            return {
                "items": pets,
                "total": total,
                "page": page,
                "page_size": page_size,
                "total_pages": total_pages
            }

        finally:

            self._close(
                connection,
                cursor
            )

    def get_by_owner_id(
            self,
            owner_id
    ) -> list[Pet]:

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                name,
                species,
                age,
                owner_id
            FROM Pets
            WHERE owner_id = ?
            """

            cursor.execute(
                query,
                (
                    owner_id,
                )
            )

            rows = cursor.fetchall()

            pets = []

            for row in rows:

                pets.append(
                    Pet(
                        name=row.name,
                        species=row.species,
                        age=row.age,
                        owner_id=row.owner_id,
                        pet_id=row.id
                    )
                )

            return pets

        finally:

            self._close(
                connection,
                cursor
            )