from fastapi import (
    Depends,
    HTTPException
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from jose import (
    jwt,
    JWTError
)

from config.settings import (
    JWT_SECRET,
    JWT_ALGORITHM
)

from auth.roles import (
    ADMIN_ROLE_ID,
    VETERINARIAN_ROLE_ID,
    RECEPTIONIST_ROLE_ID
)

security = HTTPBearer()


def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(
            security
        )
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[
                JWT_ALGORITHM
            ]
        )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )


def require_authenticated_user(
        current_user=Depends(
            get_current_user
        )
):

    return current_user


def require_admin(
        current_user=Depends(
            get_current_user
        )
):

    if current_user["role_id"] != ADMIN_ROLE_ID:

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return current_user


def require_admin_or_veterinarian(
        current_user=Depends(
            get_current_user
        )
):

    if current_user["role_id"] not in [
        ADMIN_ROLE_ID,
        VETERINARIAN_ROLE_ID
    ]:

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return current_user


def require_admin_or_receptionist(
        current_user=Depends(
            get_current_user
        )
):

    if current_user["role_id"] not in [
        ADMIN_ROLE_ID,
        RECEPTIONIST_ROLE_ID
    ]:

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return current_user