from fastapi import (
    APIRouter,
    Depends,
    Query
)

from models.appointments import Appointment

from services.appointment_service import (
    AppointmentService
)

from app.dependencies import (
    get_appointment_service
)

from api.schemas.appointment_schema import (
    AppointmentCreate,
    AppointmentUpdate,
    AppointmentResponse,
    AppointmentWithPetResponse,
    PaginatedAppointmentWithPetResponse
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
    "/paginated",
    response_model=PaginatedAppointmentWithPetResponse
)
def get_paginated_appointments(
        page: int = Query(
            1,
            ge=1
        ),
        page_size: int = Query(
            10,
            ge=1,
            le=100
        ),
        search: str | None = Query(
            None
        ),
        pet_id: int | None = Query(
            None
        ),
        date_from: str | None = Query(
            None
        ),
        date_to: str | None = Query(
            None
        ),
        current_user=Depends(
            require_authenticated_user
        ),
        appointment_service: AppointmentService = Depends(
            get_appointment_service
        )
):

    return (
        appointment_service
        .get_paginated_appointments_with_pet(
            page=page,
            page_size=page_size,
            search=search,
            pet_id=pet_id,
            date_from=date_from,
            date_to=date_to
        )
    )


@router.get(
    "/search/{pet_id}"
)
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
        )
):

    appointment = Appointment(
        pet_id=appointment_data.pet_id,
        appointment_date=(
            appointment_data.appointment_date
        ),
        reason=appointment_data.reason
    )

    appointment_id = (
        appointment_service.create_appointment(
            appointment,
            current_user["user_id"]
        )
    )

    return success_response(
        "Appointment created successfully",
        {
            "id": appointment_id
        }
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
        )
):

    updated_appointment_id = (
        appointment_service.update_appointment(
            appointment_id,
            appointment_data.appointment_date,
            appointment_data.reason,
            current_user["user_id"]
        )
    )

    return success_response(
        "Appointment updated successfully",
        {
            "id": updated_appointment_id
        }
    )


@router.delete("/{appointment_id}")
def delete_appointment(
        appointment_id: int,
        current_user=Depends(
            require_admin
        ),
        appointment_service: AppointmentService = Depends(
            get_appointment_service
        )
):

    deleted_appointment_id = (
        appointment_service.delete_appointment(
            appointment_id,
            current_user["user_id"]
        )
    )

    return success_response(
        "Appointment deleted successfully",
        {
            "id": deleted_appointment_id
        }
    )