from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from api.routes.pet_routes import (
    router as pet_router
)

from api.routes.owner_routes import (
    router as owner_router
)

from api.routes.appointment_routes import (
    router as appointment_router
)

from api.routes.dashboard_routes import (
    router as dashboard_router
)

from api.routes.auth_routes import (
    router as auth_router
)

from api.routes.medical_record_routes import (
    router as medical_record_router
)

from api.routes.audit_log_routes import (
    router as audit_log_router
)

from api.routes.user_routes import (
    router as user_router
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
    - Medical Records
    - Audit Logs
    - Users
    - Authentication

    Built with FastAPI and SQL Server.
    """,
    version="1.0.0"
)

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

register_exception_handlers(
    app
)

app.include_router(
    auth_router,
    prefix="/api/v1"
)

app.include_router(
    pet_router,
    prefix="/api/v1"
)

app.include_router(
    owner_router,
    prefix="/api/v1"
)

app.include_router(
    appointment_router,
    prefix="/api/v1"
)

app.include_router(
    medical_record_router,
    prefix="/api/v1"
)

app.include_router(
    audit_log_router,
    prefix="/api/v1"
)

app.include_router(
    user_router,
    prefix="/api/v1"
)

app.include_router(
    dashboard_router,
    prefix="/api/v1"
)