from pydantic import BaseModel
from datetime import datetime


class RecentAppointmentResponse(
    BaseModel
):

    id: int
    pet_id: int
    pet_name: str
    appointment_date: datetime
    reason: str


class DashboardResponse(
    BaseModel
):

    total_owners: int
    total_pets: int
    total_appointments: int

    recent_appointments: list[
        RecentAppointmentResponse
    ]