from fastapi import (
    APIRouter,
    Depends
)

from models.owner import Owner

from services.owner_service import (
    OwnerService
)

from app.dependencies import (
    get_owner_service
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
        )
):

    owner = Owner(
        name=owner_data.name,
        phone=owner_data.phone
    )

    owner_id = (
        owner_service.create_owner(
            owner,
            current_user["user_id"]
        )
    )

    return success_response(
        "Owner created successfully",
        {
            "id": owner_id
        }
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
        )
):

    updated_owner_id = (
        owner_service.update_owner(
            owner_id,
            owner_data.name,
            owner_data.phone,
            current_user["user_id"]
        )
    )

    return success_response(
        "Owner updated successfully",
        {
            "id": updated_owner_id
        }
    )


@router.delete("/{owner_id}")
def delete_owner(
        owner_id: int,
        current_user=Depends(
            require_admin
        ),
        owner_service: OwnerService = Depends(
            get_owner_service
        )
):

    deleted_owner_id = (
        owner_service.delete_owner(
            owner_id,
            current_user["user_id"]
        )
    )

    return success_response(
        "Owner deleted successfully",
        {
            "id": deleted_owner_id
        }
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