from pydantic import BaseModel


class PetCreate(BaseModel):

    name: str
    species: str
    age: int
    owner_id: int