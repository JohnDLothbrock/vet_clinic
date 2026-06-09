from fastapi import (
    APIRouter,
    Depends
)

from services.auth_service import (
    AuthService
)

from services.password_reset_service import (
    PasswordResetService
)

from app.dependencies import (
    get_auth_service,
    get_password_reset_service
)

from api.schemas.auth_schema import (
    LoginRequest,
    LoginResponse,
    ForgotPasswordRequest,
    ResetPasswordRequest,
    PasswordResetResponse
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


@router.post(
    "/forgot-password",
    response_model=PasswordResetResponse
)
def forgot_password(
        forgot_password_data: ForgotPasswordRequest,
        password_reset_service: PasswordResetService = Depends(
            get_password_reset_service
        )
):

    return (
        password_reset_service
        .request_password_reset(
            forgot_password_data.email
        )
    )


@router.post(
    "/reset-password",
    response_model=PasswordResetResponse
)
def reset_password(
        reset_password_data: ResetPasswordRequest,
        password_reset_service: PasswordResetService = Depends(
            get_password_reset_service
        )
):

    return (
        password_reset_service
        .reset_password(
            reset_password_data.token,
            reset_password_data.new_password
        )
    )