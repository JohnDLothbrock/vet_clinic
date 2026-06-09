from fastapi import (
    APIRouter,
    Depends
)

from services.audit_log_service import (
    AuditLogService
)

from app.dependencies import (
    get_audit_log_service
)

from api.schemas.audit_log_schema import (
    AuditLogResponse
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