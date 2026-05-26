from database.connection import get_connection
from models.pet import Pet


class PetRepository:


    # CREATE
    def create(self, pet: Pet) -> None:

        connection = get_connection()
        cursor = connection.cursor()

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

        cursor.close()
        connection.close()

    # READ ALL
    def get_all(self) -> list[Pet]:

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT id,
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

            pet = Pet(
                name=row.name,
                species=row.species,
                age=row.age,
                owner_id=row.owner_id,
                pet_id=row.id
            )

            pets.append(pet)

        cursor.close()
        connection.close()

        return pets

    # READ ONE
    def get_by_id(
        self,
        pet_id: int
    ) -> Pet | None:

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT id,
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

        cursor.close()
        connection.close()

        if row is None:
            return None

        return Pet(
            name=row.name,
            species=row.species,
            age=row.age,
            owner_id=row.owner_id,
            pet_id=row.id
        )

    # UPDATE
    def update(
        self,
        pet_id: int,
        name: str,
        species: str,
        age: int
    ) -> None:

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        UPDATE Pets
        SET name = ?,
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

        cursor.close()
        connection.close()

    # DELETE
    def delete(
        self,
        pet_id: int
    ) -> None:

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        DELETE FROM Pets
        WHERE id = ?
        """

        cursor.execute(
            query,
            (pet_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()


    def get_by_name(
            self,
            name
    ):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
                SELECT id,
                       name,
                       species,
                       age,
                       owner_id
                FROM Pets
                WHERE name LIKE ? \
                """

        cursor.execute(
            query,
            (f"%{name}%",)
        )

        rows = cursor.fetchall()

        pets = []

        for row in rows:
            pet = Pet(
                name=row[1],
                species=row[2],
                age=row[3],
                owner_id=row[4],
                pet_id=row[0]
            )

            pets.append(pet)

        cursor.close()
        connection.close()

        return pets