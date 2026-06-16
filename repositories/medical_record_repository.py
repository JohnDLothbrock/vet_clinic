from math import ceil

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
    ) -> int:

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
            OUTPUT INSERTED.id
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
                        weight=(
                            float(row.weight)
                            if row.weight is not None
                            else 0
                        ),
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
                (
                    medical_record_id,
                )
            )

            row = cursor.fetchone()

            if row is None:

                return None

            return MedicalRecord(
                pet_id=row.pet_id,
                visit_date=str(row.visit_date),
                weight=(
                    float(row.weight)
                    if row.weight is not None
                    else 0
                ),
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
                (
                    medical_record_id,
                )
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
            WHERE pet_id = ?
            ORDER BY visit_date DESC
            """

            cursor.execute(
                query,
                (
                    pet_id,
                )
            )

            rows = cursor.fetchall()

            records = []

            for row in rows:

                records.append(
                    MedicalRecord(
                        pet_id=row.pet_id,
                        visit_date=str(row.visit_date),
                        weight=(
                            float(row.weight)
                            if row.weight is not None
                            else 0
                        ),
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

    def get_paginated(
            self,
            page: int,
            page_size: int,
            search: str | None = None,
            pet_id: int | None = None,
            date_from: str | None = None,
            date_to: str | None = None
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
                        mr.diagnosis LIKE ?
                        OR mr.treatment LIKE ?
                        OR mr.notes LIKE ?
                        OR p.name LIKE ?
                    )
                    """
                )

                search_value = f"%{search}%"

                params.extend(
                    [
                        search_value,
                        search_value,
                        search_value,
                        search_value
                    ]
                )

            if pet_id:

                where_clauses.append(
                    "mr.pet_id = ?"
                )

                params.append(
                    pet_id
                )

            if date_from:

                where_clauses.append(
                    "mr.visit_date >= ?"
                )

                params.append(
                    date_from
                )

            if date_to:

                where_clauses.append(
                    "mr.visit_date <= ?"
                )

                params.append(
                    date_to
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
            FROM MedicalRecords mr
            INNER JOIN Pets p
                ON mr.pet_id = p.id
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
                mr.id,
                mr.pet_id,
                mr.visit_date,
                mr.weight,
                mr.diagnosis,
                mr.treatment,
                mr.notes,
                mr.created_by
            FROM MedicalRecords mr
            INNER JOIN Pets p
                ON mr.pet_id = p.id
            {where_sql}
            ORDER BY mr.visit_date DESC
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

            records = []

            for row in rows:

                records.append(
                    {
                        "id": row.id,
                        "pet_id": row.pet_id,
                        "visit_date": str(row.visit_date),
                        "weight": (
                            float(row.weight)
                            if row.weight is not None
                            else 0
                        ),
                        "diagnosis": row.diagnosis,
                        "treatment": row.treatment,
                        "notes": row.notes,
                        "created_by": row.created_by
                    }
                )

            total_pages = (
                ceil(total / page_size)
                if total > 0
                else 0
            )

            return {
                "items": records,
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