from models.audit_log import AuditLog

from utils.logger import logger


class AuditLogService:

    def __init__(
            self,
            audit_log_repository
    ):

        self.audit_log_repository = (
            audit_log_repository
        )

    def create_audit_log(
            self,
            user_id,
            action,
            entity,
            entity_id
    ):

        audit_log = AuditLog(
            user_id=user_id,
            action=action,
            entity=entity,
            entity_id=entity_id
        )

        self.audit_log_repository.create(
            audit_log
        )

        logger.info(
            (
                f"Audit log created: "
                f"user_id={user_id}, "
                f"action={action}, "
                f"entity={entity}, "
                f"entity_id={entity_id}"
            )
        )

    def get_all_audit_logs(self):

        return (
            self.audit_log_repository
            .get_all()
        )

    def get_paginated_audit_logs(
            self,
            page: int,
            page_size: int,
            action: str | None = None,
            entity: str | None = None,
            user_id: int | None = None,
            date_from: str | None = None,
            date_to: str | None = None
    ):

        logger.info(
            "Fetching paginated audit logs"
        )

        if page < 1:

            page = 1

        if page_size < 1:

            page_size = 10

        if page_size > 100:

            page_size = 100

        return (
            self.audit_log_repository
            .get_paginated(
                page=page,
                page_size=page_size,
                action=action,
                entity=entity,
                user_id=user_id,
                date_from=date_from,
                date_to=date_to
            )
        )

    def get_audit_logs_by_entity(
            self,
            entity,
            entity_id
    ):

        return (
            self.audit_log_repository
            .get_by_entity(
                entity,
                entity_id
            )
        )