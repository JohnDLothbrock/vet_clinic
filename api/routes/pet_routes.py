from fastapi import (
    APIRouter,
    Depends
)

from models.pet import Pet

from services.pet_service import (
    PetService
)

from services.audit_log_service import (
    AuditLogService
)

from app.dependencies import (
    get_pet_service,
    get_audit_log_service
)

from api.schemas.pet_schema import (
    PetCreate,
    PetUpdate,
    PetResponse,
    PetWithOwnerResponse
)

from utils.api_response import (
    success_response
)

from auth.current_user import (
    require_authenticated_user,
    require_admin_or_receptionist,
    require_admin
)

router = APIRouter(
    prefix="/pets",
    tags=["Pets"]
)


@router.get(
    "",
    response_model=list[PetResponse]
)
def get_pets(
        current_user=Depends(
            require_authenticated_user
        ),
        pet_service: PetService = Depends(
            get_pet_service
        )
):

    return (
        pet_service.get_all_pets()
    )


@router.get(
    "/with-owner",
    response_model=list[PetWithOwnerResponse]
)
def get_pets_with_owner(
        current_user=Depends(
            require_authenticated_user
        ),
        pet_service: PetService = Depends(
            get_pet_service
        )
):

    return (
        pet_service
        .get_all_pets_with_owner()
    )


@router.get(
    "/search/{name}",
    response_model=list[PetWithOwnerResponse]
)
def search_pets(
        name: str,
        current_user=Depends(
            require_authenticated_user
        ),
        pet_service: PetService = Depends(
            get_pet_service
        )
):

    return (
        pet_service.search_pets_by_name(
            name
        )
    )


@router.get(
    "/{pet_id}",
    response_model=PetResponse
)
def get_pet_by_id(
        pet_id: int,
        current_user=Depends(
            require_authenticated_user
        ),
        pet_service: PetService = Depends(
            get_pet_service
        )
):

    return (
        pet_service.get_pet_by_id(
            pet_id
        )
    )


@router.post("")
def create_pet(
        pet_data: PetCreate,
        current_user=Depends(
            require_admin_or_receptionist
        ),
        pet_service: PetService = Depends(
            get_pet_service
        ),
        audit_log_service: AuditLogService = Depends(
            get_audit_log_service
        )
):

    pet = Pet(
        name=pet_data.name,
        species=pet_data.species,
        age=pet_data.age,
        owner_id=pet_data.owner_id
    )

    pet_service.create_pet(
        pet
    )

    audit_log_service.create_audit_log(
        user_id=current_user["user_id"],
        action="CREATE",
        entity="Pet",
        entity_id=0
    )

    return success_response(
        "Pet created successfully"
    )


@router.put("/{pet_id}")
def update_pet(
        pet_id: int,
        pet_data: PetUpdate,
        current_user=Depends(
            require_admin_or_receptionist
        ),
        pet_service: PetService = Depends(
            get_pet_service
        ),
        audit_log_service: AuditLogService = Depends(
            get_audit_log_service
        )
):

    pet_service.update_pet(
        pet_id,
        pet_data.name,
        pet_data.species,
        pet_data.age
    )

    audit_log_service.create_audit_log(
        user_id=current_user["user_id"],
        action="UPDATE",
        entity="Pet",
        entity_id=pet_id
    )

    return success_response(
        "Pet updated successfully"
    )


@router.delete("/{pet_id}")
def delete_pet(
        pet_id: int,
        current_user=Depends(
            require_admin
        ),
        pet_service: PetService = Depends(
            get_pet_service
        ),
        audit_log_service: AuditLogService = Depends(
            get_audit_log_service
        )
):

    pet_service.delete_pet(
        pet_id
    )

    audit_log_service.create_audit_log(
        user_id=current_user["user_id"],
        action="DELETE",
        entity="Pet",
        entity_id=pet_id
    )

    return success_response(
        "Pet deleted successfully"
    )