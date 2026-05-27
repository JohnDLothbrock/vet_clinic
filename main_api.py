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
    pet_not_found_handler,
    owner_not_found_handler,
    appointment_not_found_handler,
    generic_exception_handler
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


app = FastAPI()


app.include_router(
    pet_router
)

app.include_router(
    owner_router
)

app.include_router(
    appointment_router
)


app.add_exception_handler(
    PetNotFoundException,
    pet_not_found_handler
)

app.add_exception_handler(
    OwnerNotFoundException,
    owner_not_found_handler
)

app.add_exception_handler(
    AppointmentNotFoundException,
    appointment_not_found_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)