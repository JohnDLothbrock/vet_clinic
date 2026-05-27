from fastapi import FastAPI

from api.routes.pet_routes import (
    router as pet_router
)

from api.routes.owner_routes import (
    router as owner_router
)

from api.routes.appointment_routes import (
    router as appointment_router
)

from api.handlers.exception_handlers import (
    register_exception_handlers
)

app = FastAPI(
    title="Veterinary Clinic API",
    description="""
    API for managing:

    - Pets
    - Owners
    - Appointments

    Built with FastAPI and SQL Server.
    """,
    version="1.0.0"
)

register_exception_handlers(app)

app.include_router(
    pet_router,
    prefix="/api/v1",
    tags=["Pets"]
)

app.include_router(
    owner_router,
    prefix="/api/v1",
    tags=["Owners"]
)

app.include_router(
    appointment_router,
    prefix="/api/v1",
    tags=["Appointments"]
)