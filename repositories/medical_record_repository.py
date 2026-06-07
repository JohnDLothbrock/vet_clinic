from models.medical_record import MedicalRecord

from repositories.base_repository import (
    BaseRepository
)


class MedicalRecordRepository(
    BaseRepository
):

    def create(
            self,
            medical_record: MedicalRecord
    ) -> None:

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            INSERT INTO MedicalRecords (
                pet_id,
                visit_date,
                weight,
                diagnosis,
                treatment,
                notes,
                created_by
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """

            cursor.execute(
                query,
                (
                    medical_record.pet_id,
                    medical_record.visit_date,
                    medical_record.weight,
                    medical_record.diagnosis,
                    medical_record.treatment,
                    medical_record.notes,
                    medical_record.created_by
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
    ) -> list[MedicalRecord]:

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                pet_id,
                visit_date,
                weight,
                diagnosis,
                treatment,
                notes,
                created_by
            FROM MedicalRecords
            ORDER BY visit_date DESC
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            records = []

            for row in rows:

                records.append(
                    MedicalRecord(
                        pet_id=row.pet_id,
                        visit_date=str(row.visit_date),
                        weight=float(row.weight)
                        if row.weight is not None
                        else 0,
                        diagnosis=row.diagnosis,
                        treatment=row.treatment,
                        notes=row.notes,
                        created_by=row.created_by,
                        medical_record_id=row.id
                    )
                )

            return records

        finally:

            self._close(
                connection,
                cursor
            )

    def get_by_id(
            self,
            medical_record_id: int
    ) -> MedicalRecord | None:

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                pet_id,
                visit_date,
                weight,
                diagnosis,
                treatment,
                notes,
                created_by
            FROM MedicalRecords
            WHERE id = ?
            """

            cursor.execute(
                query,
                (medical_record_id,)
            )

            row = cursor.fetchone()

            if row is None:

                return None

            return MedicalRecord(
                pet_id=row.pet_id,
                visit_date=str(row.visit_date),
                weight=float(row.weight)
                if row.weight is not None
                else 0,
                diagnosis=row.diagnosis,
                treatment=row.treatment,
                notes=row.notes,
                created_by=row.created_by,
                medical_record_id=row.id
            )

        finally:

            self._close(
                connection,
                cursor
            )

    def update(
            self,
            medical_record: MedicalRecord
    ) -> None:

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            UPDATE MedicalRecords
            SET
                visit_date = ?,
                weight = ?,
                diagnosis = ?,
                treatment = ?,
                notes = ?
            WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    medical_record.visit_date,
                    medical_record.weight,
                    medical_record.diagnosis,
                    medical_record.treatment,
                    medical_record.notes,
                    medical_record.id
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
            medical_record_id: int
    ) -> None:

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            DELETE FROM MedicalRecords
            WHERE id = ?
            """

            cursor.execute(
                query,
                (medical_record_id,)
            )

            connection.commit()

        finally:

            self._close(
                connection,
                cursor
            )

    def get_by_pet_id(
            self,
            pet_id: int
    ):

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                mr.id,
                mr.pet_id,
                p.name AS pet_name,
                mr.visit_date,
                mr.weight,
                mr.diagnosis,
                mr.treatment,
                mr.notes,
                mr.created_by
            FROM MedicalRecords mr
            INNER JOIN Pets p
                ON mr.pet_id = p.id
            WHERE mr.pet_id = ?
            ORDER BY mr.visit_date DESC
            """

            cursor.execute(
                query,
                (pet_id,)
            )

            rows = cursor.fetchall()

            records = []

            for row in rows:

                records.append({

                    "id": row.id,
                    "pet_id": row.pet_id,
                    "pet_name": row.pet_name,
                    "visit_date": row.visit_date,
                    "weight": float(row.weight)
                    if row.weight is not None
                    else 0,
                    "diagnosis": row.diagnosis,
                    "treatment": row.treatment,
                    "notes": row.notes,
                    "created_by": row.created_by
                })

            return records

        finally:

            self._close(
                connection,
                cursor
            )