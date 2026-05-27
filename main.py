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
    8. Update Owner
    9. Delete Owner
    10. Search Owner by Name

    APPOINTMENTS
    11. Add Appointment
    12. View Appointments
    13. Update Appointment
    14. Delete Appointment
    15. Search Appointments by Pet ID

    16. Exit
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

    elif option == "8":
        owner_controller.update_owner()

    elif option == "9":
        owner_controller.delete_owner()

    elif option == "10":
        owner_controller.search_owner_by_name()

    # APPOINTMENTS
    elif option == "11":
        appointment_controller.create_appointment()

    elif option == "12":
        appointment_controller.show_appointments()

    elif option == "13":
        appointment_controller.update_appointment()

    elif option == "14":
        appointment_controller.delete_appointment()

    elif option == "15":
        appointment_controller.search_appointments_by_pet_id()

    # EXIT
    elif option == "16":
        break

    else:
        print("Invalid option")