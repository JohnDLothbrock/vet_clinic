from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions.owner_not_found_exception import (
    OwnerNotFoundException
)

from exceptions.pet_not_found_exception import (
    PetNotFoundException
)

from exceptions.appointment_not_found_exception import (
    AppointmentNotFoundException
)


def register_exception_handlers(app):

    @app.exception_handler(
        OwnerNotFoundException
    )
    async def owner_not_found_handler(
            request: Request,
            exc: OwnerNotFoundException
    ):

        return JSONResponse(
            status_code=404,
            content={
                "error": str(exc)
            }
        )


    @app.exception_handler(
        PetNotFoundException
    )
    async def pet_not_found_handler(
            request: Request,
            exc: PetNotFoundException
    ):

        return JSONResponse(
            status_code=404,
            content={
                "error": str(exc)
            }
        )


    @app.exception_handler(
        AppointmentNotFoundException
    )
    async def appointment_not_found_handler(
            request: Request,
            exc: AppointmentNotFoundException
    ):

        return JSONResponse(
            status_code=404,
            content={
                "error": str(exc)
            }
        )