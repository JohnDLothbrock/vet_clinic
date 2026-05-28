from repositories.owner_repository import (
    OwnerRepository
)
from repositories.pet_repository import (
    PetRepository
)
from repositories.appointment_repository import (
    AppointmentRepository
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



# REPOSITORIES

owner_repository = OwnerRepository()

pet_repository = PetRepository()

appointment_repository = (
    AppointmentRepository()
)


# SERVICES

owner_service = OwnerService(
    owner_repository
)

pet_service = PetService(
    pet_repository,
    owner_service
)

appointment_service = AppointmentService(
    appointment_repository,
    pet_service
)


# DEPENDENCY FUNCTIONS

def get_owner_service():

    return owner_service


def get_pet_service():

    return pet_service


def get_appointment_service():

    return appointment_service

