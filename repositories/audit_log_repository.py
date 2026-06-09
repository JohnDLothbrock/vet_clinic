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