from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions.application_exception import (
    ApplicationException
)


def register_exception_handlers(app):

    @app.exception_handler(
        ApplicationException
    )
    async def application_exception_handler(
            request: Request,
            exc: ApplicationException
    ):

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": exc.message
            }
        )