from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict
)


class AuditLogResponse(
    BaseModel
):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    user_id: int
    action: str
    entity: str
    entity_id: int
    created_at: datetime


class PaginatedAuditLogResponse(
    BaseModel
):

    items: list[AuditLogResponse]
    total: int
    page: int
    page_size: int
    total_pages: int