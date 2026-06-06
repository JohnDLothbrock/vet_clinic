from fastapi import (
    Depends,
    HTTPException
)

from auth.current_user import (
    get_current_user
)

from auth.roles import (
    ADMIN_ROLE_ID,
    VETERINARIAN_ROLE_ID,
    RECEPTIONIST_ROLE_ID
)


def authenticated_user(
        current_user=Depends(
            get_current_user
        )
):

    return current_user


def admin_only(
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


def admin_or_veterinarian(
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


def admin_or_receptionist(
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