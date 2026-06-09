from repositories.owner_repository import (
    OwnerRepository
)

from repositories.pet_repository import (
    PetRepository
)

from repositories.appointment_repository import (
    AppointmentRepository
)

from repositories.user_repository import (
    UserRepository
)

from repositories.medical_record_repository import (
    MedicalRecordRepository
)

from repositories.audit_log_repository import (
    AuditLogRepository
)

from services.owner_service import (
    OwnerService
)

from services.pet_service import (
    PetService
)

from services.appointment_service import (
    AppointmentService
)

from services.dashboard_service import (
    DashboardService
)

from services.user_service import (
    UserService
)

from services.auth_service import (
    AuthService
)

from services.medical_record_service import (
    MedicalRecordService
)

from services.audit_log_service import (
    AuditLogService
)


# REPOSITORIES

owner_repository = (
    OwnerRepository()
)

pet_repository = (
    PetRepository()
)

appointment_repository = (
    AppointmentRepository()
)

user_repository = (
    UserRepository()
)

medical_record_repository = (
    MedicalRecordRepository()
)

audit_log_repository = (
    AuditLogRepository()
)


# SERVICES

owner_service = (
    OwnerService(
        owner_repository
    )
)

pet_service = (
    PetService(
        pet_repository,
        owner_service
    )
)

# Link services after creation
owner_service.pet_service = (
    pet_service
)

appointment_service = (
    AppointmentService(
        appointment_repository,
        pet_service
    )
)

dashboard_service = (
    DashboardService(
        owner_service,
        pet_service,
        appointment_service
    )
)

user_service = (
    UserService(
        user_repository
    )
)

auth_service = (
    AuthService(
        user_service
    )
)

medical_record_service = (
    MedicalRecordService(
        medical_record_repository,
        pet_service
    )
)

audit_log_service = (
    AuditLogService(
        audit_log_repository
    )
)


# DEPENDENCY FUNCTIONS

def get_owner_service():

    return owner_service


def get_pet_service():

    return pet_service


def get_appointment_service():

    return appointment_service


def get_dashboard_service():

    return dashboard_service


def get_user_service():

    return user_service


def get_auth_service():

    return auth_service


def get_medical_record_service():

    return medical_record_service


def get_audit_log_service():

    return audit_log_service