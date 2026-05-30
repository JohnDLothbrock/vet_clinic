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


router = APIRouter(
    prefix="/owners",
    tags=["Owners"]
)


@router.get(
    "",
    response_model=list[OwnerResponse]
)
def get_owners(
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
        owner_service: OwnerService = Depends(
            get_owner_service
        )
):

    owner = Owner(
        name=owner_data.name,
        phone=owner_data.phone
    )

    owner_service.create_owner(
        owner
    )

    return success_response(
        "Owner created successfully"
    )


@router.put("/{owner_id}")
def update_owner(
        owner_id: int,
        owner_data: OwnerUpdate,
        owner_service: OwnerService = Depends(
            get_owner_service
        )
):

    owner_service.update_owner(
        owner_id,
        owner_data.name,
        owner_data.phone
    )

    return success_response(
        "Owner updated successfully"
    )


@router.delete("/{owner_id}")
def delete_owner(
        owner_id: int,
        owner_service: OwnerService = Depends(
            get_owner_service
        )
):

    owner_service.delete_owner(
        owner_id
    )

    return success_response(
        "Owner deleted successfully"
    )

@router.get("/search/{name}")
def search_owners(
        name: str,
        owner_service: OwnerService = Depends(
            get_owner_service
        )
):

    return (
        owner_service.search_owners_by_name(
            name
        )
    )

