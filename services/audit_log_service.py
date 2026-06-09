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