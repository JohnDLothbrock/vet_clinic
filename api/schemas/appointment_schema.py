from pydantic import BaseModel


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
    appointment_date: str
    reason: str