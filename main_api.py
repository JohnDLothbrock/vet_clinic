from fastapi import FastAPI

from api.routes.pet_routes import (
    router as pet_router
)

app = FastAPI(
    title="Veterinary Clinic API",
    version="1.0.0"
)

app.include_router(
    pet_router
)


@app.get("/")
def home():

    return {
        "message": "Veterinary Clinic API Running"
    }