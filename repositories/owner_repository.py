from database.connection import get_connection
from models.owner import Owner


class OwnerRepository:

    def create(self, owner):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO Owners (
            name,
            phone
        )
        VALUES (?, ?)
        """

        cursor.execute(
            query,
            (
                owner.name,
                owner.phone
            )
        )

        connection.commit()

        cursor.close()
        connection.close()

    def get_all(self):

        connection = get_connection()
        cursor = connection.cursor()

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

        cursor.close()
        connection.close()

        return owners

    def get_by_id(self, owner_id):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
                SELECT id, \
                       name, \
                       phone
                FROM Owners
                WHERE id = ? \
                """

        cursor.execute(query, (owner_id,))

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        if row:
            return Owner(
                name=row.name,
                phone=row.phone,
                owner_id=row.id
            )

        return None