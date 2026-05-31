from pydantic import BaseModel


class DashboardResponse(
    BaseModel
):

    total_owners: int
    total_pets: int
    total_appointments: int

