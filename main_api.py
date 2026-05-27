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

from api.exception_handlers import (
    register_exception_handlers
)


app = FastAPI()

register_exception_handlers(
    app
)

app.include_router(pet_router)
app.include_router(owner_router)
app.include_router(appointment_router)