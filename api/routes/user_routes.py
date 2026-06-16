from fastapi import (
    APIRouter,
    Depends,
    Query
)

from services.user_service import (
    UserService
)

from app.dependencies import (
    get_user_service
)

from api.schemas.user_schema import (
    UserCreate,
    UserResponse,
    PaginatedUserResponse,
    UserRoleUpdate,
    UserActiveUpdate,
    ChangePasswordRequest
)

from utils.api_response import (
    success_response
)

from auth.current_user import (
    require_admin,
    require_authenticated_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "",
    response_model=list[UserResponse]
)
def get_users(
        current_user=Depends(
            require_admin
        ),
        user_service: UserService = Depends(
            get_user_service
        )
):

    return (
        user_service
        .get_all_users()
    )


@router.get(
    "/paginated",
    response_model=PaginatedUserResponse
)
def get_paginated_users(
        page: int = Query(
            1,
            ge=1
        ),
        page_size: int = Query(
            10,
            ge=1,
            le=100
        ),
        search: str | None = Query(
            None
        ),
        role_id: int | None = Query(
            None
        ),
        active: bool | None = Query(
            None
        ),
        current_user=Depends(
            require_admin
        ),
        user_service: UserService = Depends(
            get_user_service
        )
):

    return (
        user_service
        .get_paginated_users(
            page=page,
            page_size=page_size,
            search=search,
            role_id=role_id,
            active=active
        )
    )


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user_by_id(
        user_id: int,
        current_user=Depends(
            require_admin
        ),
        user_service: UserService = Depends(
            get_user_service
        )
):

    return (
        user_service
        .get_user_by_id(
            user_id
        )
    )


@router.post("")
def create_user(
        user_data: UserCreate,
        current_user=Depends(
            require_admin
        ),
        user_service: UserService = Depends(
            get_user_service
        )
):

    user_id = (
        user_service
        .create_user(
            user_data.username,
            user_data.email,
            user_data.password,
            user_data.role_id
        )
    )

    return success_response(
        "User created successfully",
        {
            "id": user_id
        }
    )


@router.put("/{user_id}/role")
def update_user_role(
        user_id: int,
        user_data: UserRoleUpdate,
        current_user=Depends(
            require_admin
        ),
        user_service: UserService = Depends(
            get_user_service
        )
):

    updated_user_id = (
        user_service
        .update_user_role(
            user_id,
            user_data.role_id
        )
    )

    return success_response(
        "User role updated successfully",
        {
            "id": updated_user_id
        }
    )


@router.put("/{user_id}/active")
def update_user_active(
        user_id: int,
        user_data: UserActiveUpdate,
        current_user=Depends(
            require_admin
        ),
        user_service: UserService = Depends(
            get_user_service
        )
):

    updated_user_id = (
        user_service
        .update_user_active(
            user_id,
            user_data.active
        )
    )

    return success_response(
        "User active status updated successfully",
        {
            "id": updated_user_id
        }
    )


@router.put("/me/change-password")
def change_my_password(
        password_data: ChangePasswordRequest,
        current_user=Depends(
            require_authenticated_user
        ),
        user_service: UserService = Depends(
            get_user_service
        )
):

    return (
        user_service
        .change_password(
            current_user["user_id"],
            password_data.current_password,
            password_data.new_password
        )
    )