from pydantic import BaseModel


class OwnerCreate(
    BaseModel
):

    name: str
    phone: str


class OwnerUpdate(
    BaseModel
):

    name: str
    phone: str


class OwnerResponse(
    BaseModel
):

    id: int
    name: str
    phone: str