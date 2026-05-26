from database.connection import (
    get_connection
)

from app.bootstrap import (
    build_application
)


def test_connection():

    try:

        connection = get_connection()

        print(
            "Database connected successfully!"
        )

        connection.close()

    except Exception as error:

        print(
            "Connection error:",
            error
        )


test_connection()

controllers = build_application()

pet_controller = (
    controllers["pet_controller"]
)

owner_controller = (
    controllers["owner_controller"]
)

appointment_controller = (
    controllers["appointment_controller"]
)

while True:
    print("""
    --- VETERINARY CLINIC ---

    PETS
    1. Add Pet
    2. View Pets
    3. Update Pet
    4. Delete Pet
    5. Search Pet by Name

    OWNERS
    6. Add Owner
    7. View Owners

    APPOINTMENTS
    8. Add Appointment
    9. View Appointments
    10. Update Appointment
    11. Delete Appointment

    12. Exit
        """)

    option = input("Choose option: ")

    # PETS
    if option == "1":
        pet_controller.create_pet()

    elif option == "2":
        pet_controller.show_pets()

    elif option == "3":
        pet_controller.update_pet()

    elif option == "4":
        pet_controller.delete_pet()

    elif option == "5":
        pet_controller.search_pet_by_name()

    # OWNERS
    elif option == "6":
        owner_controller.create_owner()

    elif option == "7":
        owner_controller.show_owners()

    # APPOINTMENTS
    elif option == "8":
        appointment_controller.create_appointment()

    elif option == "9":
        appointment_controller.show_appointments()

    elif option == "10":
        appointment_controller.update_appointment()

    elif option == "11":
        appointment_controller.delete_appointment()

    # EXIT
    elif option == "12":
        break

    else:
        print("Invalid option")