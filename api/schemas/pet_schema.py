from pydantic import BaseModel


class PetCreate(
    BaseModel
):


    name: str
    species: str
    age: int
    owner_id: int


class PetUpdate(
    BaseModel
):


    name: str
    species: str
    age: int


class PetResponse(
    BaseModel
):


    id: int
    name: str
    species: str
    age: int
    owner_id: int


class PetWithOwnerResponse(
    BaseModel
):


    id: int
    name: str
    species: str
    age: int
    owner_id: int
    owner_name: str

