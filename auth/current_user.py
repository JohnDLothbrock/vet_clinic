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
    ADMIN_ROLE,
    RECEPTIONIST_ROLE
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
        user=Depends(
            get_current_user
        )
):

    return user


def require_admin(
        user=Depends(
            get_current_user
        )
):

    if user["role_id"] != ADMIN_ROLE:

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return user


def require_admin_or_receptionist(
        user=Depends(
            get_current_user
        )
):

    if user["role_id"] not in [
        ADMIN_ROLE,
        RECEPTIONIST_ROLE
    ]:

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return user