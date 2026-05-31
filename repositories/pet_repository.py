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
    ) -> None:

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

            connection.commit()

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
                (pet_id,)
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
                (pet_id,)
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
                (f"%{name}%",)
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


    def get_all_with_owner(self):

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
                    SELECT p.id, \
                           p.name, \
                           p.species, \
                           p.age, \
                           p.owner_id, \
                           o.name AS owner_name
                    FROM Pets p
                             INNER JOIN Owners o
                                        ON p.owner_id = o.id \
                    """

            cursor.execute(query)

            rows = cursor.fetchall()

            pets = []

            for row in rows:
                pets.append({
                    "id": row.id,
                    "name": row.name,
                    "species": row.species,
                    "age": row.age,
                    "owner_id": row.owner_id,
                    "owner_name": row.owner_name
                })

            return pets

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
                    SELECT id, \
                           name, \
                           species, \
                           age, \
                           owner_id
                    FROM Pets
                    WHERE owner_id = ? \
                    """

            cursor.execute(
                query,
                (owner_id,)
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

