from fastapi import (
    APIRouter,
    Depends
)

from models.owner import Owner

from services.owner_service import (
    OwnerService
)

from services.audit_log_service import (
    AuditLogService
)

from app.dependencies import (
    get_owner_service,
    get_audit_log_service
)

from api.schemas.owner_schema import (
    OwnerCreate,
    OwnerUpdate,
    OwnerResponse
)

from utils.api_response import (
    success_response
)

from auth.current_user import (
    require_admin,
    require_admin_or_receptionist,
    require_authenticated_user
)

router = APIRouter(
    prefix="/owners",
    tags=["Owners"]
)


@router.get(
    "",
    response_model=list[OwnerResponse]
)
def get_owners(
        current_user=Depends(
            require_authenticated_user
        ),
        owner_service: OwnerService = Depends(
            get_owner_service
        )
):

    return owner_service.get_all_owners()


@router.get(
    "/{owner_id}",
    response_model=OwnerResponse
)
def get_owner_by_id(
        owner_id: int,
        current_user=Depends(
            require_authenticated_user
        ),
        owner_service: OwnerService = Depends(
            get_owner_service
        )
):

    return owner_service.get_owner_by_id(
        owner_id
    )


@router.post("")
def create_owner(
        owner_data: OwnerCreate,
        current_user=Depends(
            require_admin_or_receptionist
        ),
        owner_service: OwnerService = Depends(
            get_owner_service
        ),
        audit_log_service: AuditLogService = Depends(
            get_audit_log_service
        )
):

    owner = Owner(
        name=owner_data.name,
        phone=owner_data.phone
    )

    owner_service.create_owner(
        owner
    )

    audit_log_service.create_audit_log(
        user_id=current_user["user_id"],
        action="CREATE",
        entity="Owner",
        entity_id=0
    )

    return success_response(
        "Owner created successfully"
    )


@router.put("/{owner_id}")
def update_owner(
        owner_id: int,
        owner_data: OwnerUpdate,
        current_user=Depends(
            require_admin_or_receptionist
        ),
        owner_service: OwnerService = Depends(
            get_owner_service
        ),
        audit_log_service: AuditLogService = Depends(
            get_audit_log_service
        )
):

    owner_service.update_owner(
        owner_id,
        owner_data.name,
        owner_data.phone
    )

    audit_log_service.create_audit_log(
        user_id=current_user["user_id"],
        action="UPDATE",
        entity="Owner",
        entity_id=owner_id
    )

    return success_response(
        "Owner updated successfully"
    )


@router.delete("/{owner_id}")
def delete_owner(
        owner_id: int,
        current_user=Depends(
            require_admin
        ),
        owner_service: OwnerService = Depends(
            get_owner_service
        ),
        audit_log_service: AuditLogService = Depends(
            get_audit_log_service
        )
):

    owner_service.delete_owner(
        owner_id
    )

    audit_log_service.create_audit_log(
        user_id=current_user["user_id"],
        action="DELETE",
        entity="Owner",
        entity_id=owner_id
    )

    return success_response(
        "Owner deleted successfully"
    )


@router.get("/search/{name}")
def search_owners(
        name: str,
        current_user=Depends(
            require_authenticated_user
        ),
        owner_service: OwnerService = Depends(
            get_owner_service
        )
):

    return (
        owner_service.search_owners_by_name(
            name
        )
    )