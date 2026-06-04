from pydantic import (
    BaseModel,
    ConfigDict
)

from datetime import datetime


class AppointmentCreate(
    BaseModel
):

    pet_id: int
    appointment_date: str
    reason: str


class AppointmentUpdate(
    BaseModel
):

    appointment_date: str
    reason: str


class AppointmentResponse(
    BaseModel
):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    pet_id: int
    appointment_date: datetime
    reason: str


class AppointmentWithPetResponse(
    BaseModel
):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    pet_id: int
    pet_name: str
    appointment_date: datetime
    reason: str