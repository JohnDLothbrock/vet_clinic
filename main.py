from database.connection import get_connection
from controllers.pet_controller import PetController
from controllers.owner_controller import OwnerController
from controllers.appointment_controller import (
    AppointmentController
)
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


try:
    conn = get_connection()
    print("Database connected successfully!")
except Exception as e:
    print("Connection error:", e)


# Repositories
owner_repository = OwnerRepository()
pet_repository = PetRepository()
appointment_repository = AppointmentRepository()

# Services
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

# Controllers
controller = PetController(
    pet_service
)
owner_controller = OwnerController(
    owner_service
)
appointment_controller = AppointmentController(
    appointment_service
)

while True:
    print("""
    --- VETERINARY CLINIC ---

    PETS
    1. Add Pet
    2. View Pets
    3. Update Pet
    4. Delete Pet

    OWNERS
    5. Add Owner
    6. View Owners

    APPOINTMENTS
    7. Add Appointment
    8. View Appointments
    9. Update Appointment
    10. Delete Appointment

    11. Exit
        """)


    option = input("Choose option: ")

    if option == "1":
        controller.create_pet()

    elif option == "2":
        controller.show_pets()

    elif option == "3":
        controller.update_pet()

    elif option == "4":
        controller.delete_pet()

    elif option == "5":
        owner_controller.create_owner()

    elif option == "6":
        owner_controller.show_owners()

    elif option == "7":
        appointment_controller.create_appointment()

    elif option == "8":
        appointment_controller.show_appointments()

    elif option == "9":
        appointment_controller.update_appointment()

    elif option == "10":
        appointment_controller.delete_appointment()

    elif option == "11":
        break

    else:
        print("Invalid option")

