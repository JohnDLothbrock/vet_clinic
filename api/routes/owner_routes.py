from fastapi import APIRouter

from models.owner import Owner

from app.bootstrap import (
    build_services
)

from api.schemas.owner_schema import (
    OwnerCreate,
    OwnerUpdate,
    OwnerResponse
)

from api.utils.api_response import (
    success_response
)


router = APIRouter(
    prefix="/owners",
    tags=["Owners"]
)

services = build_services()

owner_service = services["owner_service"]


@router.get(
    "",
    response_model=list[OwnerResponse]
)
def get_owners():

    return owner_service.get_all_owners()


@router.get(
    "/{owner_id}",
    response_model=OwnerResponse
)
def get_owner_by_id(
        owner_id: int
):

    return owner_service.get_owner_by_id(
        owner_id
    )


@router.post("")
def create_owner(
        owner_data: OwnerCreate
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
        owner_data: OwnerUpdate
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
        owner_id: int
):

    owner_service.delete_owner(
        owner_id
    )

    return success_response(
        "Owner deleted successfully"
    )