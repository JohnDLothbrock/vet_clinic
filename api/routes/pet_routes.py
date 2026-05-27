from fastapi import APIRouter

from app.bootstrap import (
    build_services
)

router = APIRouter()

services = build_services()

pet_service = services["pet_service"]


@router.get("/pets")
def get_pets():

    pets = pet_service.get_all_pets()

    result = []

    for pet in pets:

        result.append(
            {
                "id": pet.id,
                "name": pet.name,
                "species": pet.species,
                "age": pet.age,
                "owner_id": pet.owner_id
            }
        )

    return result