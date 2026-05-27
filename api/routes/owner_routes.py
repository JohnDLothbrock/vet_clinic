from fastapi import (
    APIRouter,
    HTTPException
)

from models.owner import Owner

from app.bootstrap import (
    build_services
)

from api.schemas.owner_schema import (
    OwnerCreate,
    OwnerUpdate,
    OwnerResponse
)


router = APIRouter()

services = build_services()

owner_service = services["owner_service"]


@router.get(
    "/owners",
    response_model=list[OwnerResponse]
)
def get_owners():

    return owner_service.get_all_owners()


@router.get(
    "/owners/{owner_id}",
    response_model=OwnerResponse
)
def get_owner_by_id(
        owner_id: int
):

    owner = owner_service.get_owner_by_id(
        owner_id
    )

    if owner is None:

        raise HTTPException(
            status_code=404,
            detail="Owner not found"
        )

    return owner


@router.post("/owners")
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

    return {
        "message": "Owner created successfully"
    }


@router.put("/owners/{owner_id}")
def update_owner(
        owner_id: int,
        owner_data: OwnerUpdate
):

    owner_service.update_owner(
        owner_id,
        owner_data.name,
        owner_data.phone
    )

    return {
        "message": "Owner updated successfully"
    }


@router.delete("/owners/{owner_id}")
def delete_owner(
        owner_id: int
):

    owner_service.delete_owner(
        owner_id
    )

    return {
        "message": "Owner deleted successfully"
    }