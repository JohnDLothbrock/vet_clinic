from datetime import datetime

from pydantic import BaseModel


class AuditLogResponse(
    BaseModel
):

    id: int
    user_id: int
    action: str
    entity: str
    entity_id: int
    created_at: datetime