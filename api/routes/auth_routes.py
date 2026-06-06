from fastapi import (
    APIRouter,
    Depends
)

from services.auth_service import (
    AuthService
)

from app.dependencies import (
    get_auth_service
)

from api.schemas.auth_schema import (
    LoginRequest,
    LoginResponse
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
        login_data: LoginRequest,
        auth_service: AuthService = Depends(
            get_auth_service
        )
):

    return auth_service.login(
        login_data.username,
        login_data.password
    )