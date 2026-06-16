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


class PaginatedOwnerResponse(
    BaseModel
):

    items: list[OwnerResponse]
    total: int
    page: int
    page_size: int
    total_pages: int