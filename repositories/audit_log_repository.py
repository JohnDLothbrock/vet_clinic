from math import ceil

from models.audit_log import AuditLog

from repositories.base_repository import (
    BaseRepository
)


class AuditLogRepository(
    BaseRepository
):

    def create(
            self,
            audit_log: AuditLog
    ) -> None:

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            INSERT INTO AuditLog (
                user_id,
                action,
                entity,
                entity_id,
                created_at
            )
            VALUES (?, ?, ?, ?, SYSDATETIME())
            """

            cursor.execute(
                query,
                (
                    audit_log.user_id,
                    audit_log.action,
                    audit_log.entity,
                    audit_log.entity_id
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
    ):

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                user_id,
                action,
                entity,
                entity_id,
                created_at
            FROM AuditLog
            ORDER BY created_at DESC
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            audit_logs = []

            for row in rows:

                audit_logs.append(
                    AuditLog(
                        user_id=row.user_id,
                        action=row.action,
                        entity=row.entity,
                        entity_id=row.entity_id,
                        created_at=row.created_at,
                        audit_log_id=row.id
                    )
                )

            return audit_logs

        finally:

            self._close(
                connection,
                cursor
            )

    def get_by_entity(
            self,
            entity,
            entity_id
    ):

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT
                id,
                user_id,
                action,
                entity,
                entity_id,
                created_at
            FROM AuditLog
            WHERE entity = ?
            AND entity_id = ?
            ORDER BY created_at DESC
            """

            cursor.execute(
                query,
                (
                    entity,
                    entity_id
                )
            )

            rows = cursor.fetchall()

            audit_logs = []

            for row in rows:

                audit_logs.append(
                    AuditLog(
                        user_id=row.user_id,
                        action=row.action,
                        entity=row.entity,
                        entity_id=row.entity_id,
                        created_at=row.created_at,
                        audit_log_id=row.id
                    )
                )

            return audit_logs

        finally:

            self._close(
                connection,
                cursor
            )

    def get_paginated(
            self,
            page: int,
            page_size: int,
            action: str | None = None,
            entity: str | None = None,
            user_id: int | None = None,
            date_from: str | None = None,
            date_to: str | None = None
    ):

        connection = self._get_connection()
        cursor = connection.cursor()

        try:

            where_clauses = []
            params = []

            if action:

                where_clauses.append(
                    "action = ?"
                )

                params.append(
                    action
                )

            if entity:

                where_clauses.append(
                    "entity = ?"
                )

                params.append(
                    entity
                )

            if user_id:

                where_clauses.append(
                    "user_id = ?"
                )

                params.append(
                    user_id
                )

            if date_from:

                where_clauses.append(
                    "created_at >= ?"
                )

                params.append(
                    date_from
                )

            if date_to:

                where_clauses.append(
                    "created_at <= ?"
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
            FROM AuditLog
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
                user_id,
                action,
                entity,
                entity_id,
                created_at
            FROM AuditLog
            {where_sql}
            ORDER BY created_at DESC
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

            audit_logs = []

            for row in rows:

                audit_logs.append(
                    {
                        "id": row.id,
                        "user_id": row.user_id,
                        "action": row.action,
                        "entity": row.entity,
                        "entity_id": row.entity_id,
                        "created_at": row.created_at
                    }
                )

            total_pages = (
                ceil(total / page_size)
                if total > 0
                else 0
            )

            return {
                "items": audit_logs,
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