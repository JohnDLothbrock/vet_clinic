from fastapi import APIRouter

from models.appointments import Appointment

from app.bootstrap import (
    build_services
)

from api.schemas.appointment_schema import (
    AppointmentCreate,
    AppointmentUpdate,
    AppointmentResponse
)

from api.utils.api_response import (
    success_response
)


router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)

services = build_services()

appointment_service = (
    services["appointment_service"]
)


@router.get(
    "",
    response_model=list[AppointmentResponse]
)
def get_appointments():

    return (
        appointment_service
        .get_all_appointments()
    )


@router.get(
    "/{appointment_id}",
    response_model=AppointmentResponse
)
def get_appointment_by_id(
        appointment_id: int
):

    return (
        appointment_service
        .get_appointment_by_id(
            appointment_id
        )
    )


@router.post("")
def create_appointment(
        appointment_data: AppointmentCreate
):

    appointment = Appointment(
        pet_id=appointment_data.pet_id,
        appointment_date=(
            appointment_data.appointment_date
        ),
        reason=appointment_data.reason
    )

    appointment_service.create_appointment(
        appointment
    )

    return success_response(
        "Appointment created successfully"
    )


@router.put("/{appointment_id}")
def update_appointment(
        appointment_id: int,
        appointment_data: AppointmentUpdate
):

    appointment_service.update_appointment(
        appointment_id,
        appointment_data.appointment_date,
        appointment_data.reason
    )

    return success_response(
        "Appointment updated successfully"
    )


@router.delete("/{appointment_id}")
def delete_appointment(
        appointment_id: int
):

    appointment_service.delete_appointment(
        appointment_id
    )

    return success_response(
        "Appointment deleted successfully"
    )