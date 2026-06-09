from fastapi import (
    APIRouter,
    Depends
)

from models.appointments import Appointment

from services.appointment_service import (
    AppointmentService
)

from services.audit_log_service import (
    AuditLogService
)

from app.dependencies import (
    get_appointment_service,
    get_audit_log_service
)

from api.schemas.appointment_schema import (
    AppointmentCreate,
    AppointmentUpdate,
    AppointmentResponse,
    AppointmentWithPetResponse
)

from utils.api_response import (
    success_response
)

from auth.current_user import (
    require_authenticated_user,
    require_admin
)


router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)


@router.get(
    "",
    response_model=list[AppointmentResponse]
)
def get_appointments(
        current_user=Depends(
            require_authenticated_user
        ),
        appointment_service: AppointmentService = Depends(
            get_appointment_service
        )
):

    return (
        appointment_service
        .get_all_appointments()
    )


@router.get(
    "/with-pet",
    response_model=list[
        AppointmentWithPetResponse
    ]
)
def get_appointments_with_pet(
        current_user=Depends(
            require_authenticated_user
        ),
        appointment_service: AppointmentService = Depends(
            get_appointment_service
        )
):

    return (
        appointment_service
        .get_all_appointments_with_pet()
    )


@router.get(
    "/{appointment_id}",
    response_model=AppointmentResponse
)
def get_appointment_by_id(
        appointment_id: int,
        current_user=Depends(
            require_authenticated_user
        ),
        appointment_service: AppointmentService = Depends(
            get_appointment_service
        )
):

    return (
        appointment_service
        .get_appointment_by_id(
            appointment_id
        )
    )


@router.post("")
def create_appointment(
        appointment_data: AppointmentCreate,
        current_user=Depends(
            require_authenticated_user
        ),
        appointment_service: AppointmentService = Depends(
            get_appointment_service
        ),
        audit_log_service: AuditLogService = Depends(
            get_audit_log_service
        )
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

    audit_log_service.create_audit_log(
        user_id=current_user["user_id"],
        action="CREATE",
        entity="Appointment",
        entity_id=0
    )

    return success_response(
        "Appointment created successfully"
    )


@router.put("/{appointment_id}")
def update_appointment(
        appointment_id: int,
        appointment_data: AppointmentUpdate,
        current_user=Depends(
            require_authenticated_user
        ),
        appointment_service: AppointmentService = Depends(
            get_appointment_service
        ),
        audit_log_service: AuditLogService = Depends(
            get_audit_log_service
        )
):

    appointment_service.update_appointment(
        appointment_id,
        appointment_data.appointment_date,
        appointment_data.reason
    )

    audit_log_service.create_audit_log(
        user_id=current_user["user_id"],
        action="UPDATE",
        entity="Appointment",
        entity_id=appointment_id
    )

    return success_response(
        "Appointment updated successfully"
    )


@router.delete("/{appointment_id}")
def delete_appointment(
        appointment_id: int,
        current_user=Depends(
            require_admin
        ),
        appointment_service: AppointmentService = Depends(
            get_appointment_service
        ),
        audit_log_service: AuditLogService = Depends(
            get_audit_log_service
        )
):

    appointment_service.delete_appointment(
        appointment_id
    )

    audit_log_service.create_audit_log(
        user_id=current_user["user_id"],
        action="DELETE",
        entity="Appointment",
        entity_id=appointment_id
    )

    return success_response(
        "Appointment deleted successfully"
    )


@router.get("/search/{pet_id}")
def search_appointments(
        pet_id: int,
        current_user=Depends(
            require_authenticated_user
        ),
        appointment_service: AppointmentService = Depends(
            get_appointment_service
        )
):

    return (
        appointment_service
        .search_appointments_by_pet_id(
            pet_id
        )
    )