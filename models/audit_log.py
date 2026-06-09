class AuditLog:

    def __init__(
            self,
            user_id,
            action,
            entity,
            entity_id,
            created_at=None,
            audit_log_id=None
    ):

        self.id = audit_log_id
        self.user_id = user_id
        self.action = action
        self.entity = entity
        self.entity_id = entity_id
        self.created_at = created_at