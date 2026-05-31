from pydantic import BaseModel
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

    id: int
    pet_id: int
    appointment_date: datetime
    reason: str


class AppointmentWithPetResponse(
    BaseModel
):

    id: int
    pet_id: int
    pet_name: str
    appointment_date: datetime
    reason: str

