from pydantic import BaseModel


class UserCreate(
    BaseModel
):

    username: str

    email: str

    password: str

    role_id: int


class UserResponse(
    BaseModel
):

    id: int

    username: str

    email: str

    role_id: int

    active: bool


class PaginatedUserResponse(
    BaseModel
):

    items: list[UserResponse]
    total: int
    page: int
    page_size: int
    total_pages: int


class UserRoleUpdate(
    BaseModel
):

    role_id: int


class UserActiveUpdate(
    BaseModel
):

    active: bool


class ChangePasswordRequest(
    BaseModel
):

    current_password: str

    new_password: str