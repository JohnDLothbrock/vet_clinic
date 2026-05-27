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

from controllers.owner_controller import (
    OwnerController
)

from controllers.pet_controller import (
    PetController
)

from controllers.appointment_controller import (
    AppointmentController
)


def build_application():

    owner_repository = (
        OwnerRepository()
    )

    pet_repository = (
        PetRepository()
    )

    appointment_repository = (
        AppointmentRepository()
    )

    owner_service = OwnerService(
        owner_repository
    )

    pet_service = PetService(
        pet_repository,
        owner_service
    )

    appointment_service = (
        AppointmentService(
            appointment_repository,
            pet_service
        )
    )

    return {

        "pet_controller":
            PetController(
                pet_service,
                owner_service
            ),

        "owner_controller":
            OwnerController(
                owner_service
            ),

        "appointment_controller":
            AppointmentController(
                appointment_service
            )
    }

def build_services():

    owner_repository = OwnerRepository()

    pet_repository = PetRepository()

    appointment_repository = AppointmentRepository()

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

    return {
        "owner_service": owner_service,
        "pet_service": pet_service,
        "appointment_service": appointment_service
    }
