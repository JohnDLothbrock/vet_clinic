from fastapi import (
    APIRouter,
    Depends,
    Query
)

from services.audit_log_service import (
    AuditLogService
)

from app.dependencies import (
    get_audit_log_service
)

from api.schemas.audit_log_schema import (
    AuditLogResponse,
    PaginatedAuditLogResponse
)

from auth.current_user import (
    require_admin
)

router = APIRouter(
    prefix="/audit-logs",
    tags=["Audit Logs"]
)


@router.get(
    "",
    response_model=list[AuditLogResponse]
)
def get_audit_logs(
        current_user=Depends(
            require_admin
        ),
        audit_log_service: AuditLogService = Depends(
            get_audit_log_service
        )
):

    return (
        audit_log_service
        .get_all_audit_logs()
    )


@router.get(
    "/paginated",
    response_model=PaginatedAuditLogResponse
)
def get_paginated_audit_logs(
        page: int = Query(
            1,
            ge=1
        ),
        page_size: int = Query(
            10,
            ge=1,
            le=100
        ),
        action: str | None = Query(
            None
        ),
        entity: str | None = Query(
            None
        ),
        user_id: int | None = Query(
            None
        ),
        date_from: str | None = Query(
            None
        ),
        date_to: str | None = Query(
            None
        ),
        current_user=Depends(
            require_admin
        ),
        audit_log_service: AuditLogService = Depends(
            get_audit_log_service
        )
):

    return (
        audit_log_service
        .get_paginated_audit_logs(
            page=page,
            page_size=page_size,
            action=action,
            entity=entity,
            user_id=user_id,
            date_from=date_from,
            date_to=date_to
        )
    )


@router.get(
    "/{entity}/{entity_id}",
    response_model=list[AuditLogResponse]
)
def get_audit_logs_by_entity(
        entity: str,
        entity_id: int,
        current_user=Depends(
            require_admin
        ),
        audit_log_service: AuditLogService = Depends(
            get_audit_log_service
        )
):

    return (
        audit_log_service
        .get_audit_logs_by_entity(
            entity,
            entity_id
        )
    )