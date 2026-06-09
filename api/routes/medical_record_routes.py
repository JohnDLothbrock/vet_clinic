from fastapi import (
    APIRouter,
    Depends
)

from models.medical_record import (
    MedicalRecord
)

from services.medical_record_service import (
    MedicalRecordService
)

from app.dependencies import (
    get_medical_record_service
)

from api.schemas.medical_record_schema import (
    MedicalRecordCreate,
    MedicalRecordUpdate,
    MedicalRecordResponse
)

from utils.api_response import (
    success_response
)

from auth.current_user import (
    require_authenticated_user,
    require_admin_or_veterinarian,
    require_admin
)

router = APIRouter(
    prefix="/medical-records",
    tags=["Medical Records"]
)


@router.get(
    "",
    response_model=list[MedicalRecordResponse]
)
def get_medical_records(
        current_user=Depends(
            require_authenticated_user
        ),
        medical_record_service: MedicalRecordService = Depends(
            get_medical_record_service
        )
):

    return (
        medical_record_service
        .get_all_medical_records()
    )


@router.get(
    "/pet/{pet_id}",
    response_model=list[MedicalRecordResponse]
)
def get_medical_records_by_pet(
        pet_id: int,
        current_user=Depends(
            require_authenticated_user
        ),
        medical_record_service: MedicalRecordService = Depends(
            get_medical_record_service
        )
):

    return (
        medical_record_service
        .get_medical_records_by_pet(
            pet_id
        )
    )


@router.get(
    "/{medical_record_id}",
    response_model=MedicalRecordResponse
)
def get_medical_record_by_id(
        medical_record_id: int,
        current_user=Depends(
            require_authenticated_user
        ),
        medical_record_service: MedicalRecordService = Depends(
            get_medical_record_service
        )
):

    return (
        medical_record_service
        .get_medical_record_by_id(
            medical_record_id
        )
    )


@router.post("")
def create_medical_record(
        medical_record_data: MedicalRecordCreate,
        current_user=Depends(
            require_admin_or_veterinarian
        ),
        medical_record_service: MedicalRecordService = Depends(
            get_medical_record_service
        )
):

    medical_record = MedicalRecord(
        pet_id=medical_record_data.pet_id,
        visit_date=medical_record_data.visit_date,
        weight=medical_record_data.weight,
        diagnosis=medical_record_data.diagnosis,
        treatment=medical_record_data.treatment,
        notes=medical_record_data.notes,
        created_by=current_user["user_id"]
    )

    medical_record_id = (
        medical_record_service
        .create_medical_record(
            medical_record,
            current_user["user_id"]
        )
    )

    return success_response(
        "Medical record created successfully",
        {
            "id": medical_record_id
        }
    )


@router.put("/{medical_record_id}")
def update_medical_record(
        medical_record_id: int,
        medical_record_data: MedicalRecordUpdate,
        current_user=Depends(
            require_admin_or_veterinarian
        ),
        medical_record_service: MedicalRecordService = Depends(
            get_medical_record_service
        )
):

    medical_record = MedicalRecord(
        pet_id=0,
        visit_date=medical_record_data.visit_date,
        weight=medical_record_data.weight,
        diagnosis=medical_record_data.diagnosis,
        treatment=medical_record_data.treatment,
        notes=medical_record_data.notes,
        created_by=current_user["user_id"],
        medical_record_id=medical_record_id
    )

    updated_medical_record_id = (
        medical_record_service
        .update_medical_record(
            medical_record,
            current_user["user_id"]
        )
    )

    return success_response(
        "Medical record updated successfully",
        {
            "id": updated_medical_record_id
        }
    )


@router.delete("/{medical_record_id}")
def delete_medical_record(
        medical_record_id: int,
        current_user=Depends(
            require_admin
        ),
        medical_record_service: MedicalRecordService = Depends(
            get_medical_record_service
        )
):

    deleted_medical_record_id = (
        medical_record_service
        .delete_medical_record(
            medical_record_id,
            current_user["user_id"]
        )
    )

    return success_response(
        "Medical record deleted successfully",
        {
            "id": deleted_medical_record_id
        }
    )