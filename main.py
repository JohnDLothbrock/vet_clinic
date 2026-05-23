from database.connection import get_connection
from controllers.pet_controller import PetController
from controllers.owner_controller import OwnerController
from controllers.appointment_controller import (
    AppointmentController
)


try:
    conn = get_connection()
    print("Database connected successfully!")
except Exception as e:
    print("Connection error:", e)


controller = PetController()
owner_controller = OwnerController()
appointment_controller = AppointmentController()

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

    9. Exit
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
        break

    else:
        print("Invalid option")

