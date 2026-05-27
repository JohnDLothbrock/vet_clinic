from fastapi import (
    APIRouter,
    HTTPException
)

from models.pet import Pet

from app.bootstrap import (
    build_services
)

from api.schemas.pet_schema import (
    PetCreate,
    PetUpdate,
    PetResponse
)


router = APIRouter(
    prefix="/pets",
    tags=["Pets"]
)

services = build_services()

pet_service = services["pet_service"]


@router.get(
    "",
    response_model=list[PetResponse]
)
def get_pets():

    return pet_service.get_all_pets()


@router.get(
    "/{pet_id}",
    response_model=PetResponse
)
def get_pet_by_id(
        pet_id: int
):

    pet = pet_service.get_pet_by_id(
        pet_id
    )

    if pet is None:

        raise HTTPException(
            status_code=404,
            detail="Pet not found"
        )

    return pet


@router.post("")
def create_pet(
        pet_data: PetCreate
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

    return {
        "message": "Pet created successfully"
    }


@router.put("/{pet_id}")
def update_pet(
        pet_id: int,
        pet_data: PetUpdate
):

    pet_service.update_pet(
        pet_id,
        pet_data.name,
        pet_data.species,
        pet_data.age
    )

    return {
        "message": "Pet updated successfully"
    }


@router.delete("/{pet_id}")
def delete_pet(
        pet_id: int
):

    pet_service.delete_pet(
        pet_id
    )

    return {
        "message": "Pet deleted successfully"
    }