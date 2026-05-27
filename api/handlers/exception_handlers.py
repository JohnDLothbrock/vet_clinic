from fastapi import (
    Request,
    HTTPException
)

from fastapi.responses import (
    JSONResponse
)

from exceptions.pet_not_found_exception import (
    PetNotFoundException
)

from exceptions.owner_not_found_exception import (
    OwnerNotFoundException
)

from exceptions.appointment_not_found_exception import (
    AppointmentNotFoundException
)


async def pet_not_found_handler(
        request: Request,
        exception: PetNotFoundException
):

    return JSONResponse(
        status_code=404,
        content={
            "error": str(exception)
        }
    )


async def owner_not_found_handler(
        request: Request,
        exception: OwnerNotFoundException
):

    return JSONResponse(
        status_code=404,
        content={
            "error": str(exception)
        }
    )


async def appointment_not_found_handler(
        request: Request,
        exception: AppointmentNotFoundException
):

    return JSONResponse(
        status_code=404,
        content={
            "error": str(exception)
        }
    )


async def generic_exception_handler(
        request: Request,
        exception: Exception
):

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error"
        }
    )