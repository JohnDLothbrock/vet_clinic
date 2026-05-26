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
        pet_controller.create_pet()

    elif option == "2":
        pet_controller.show_pets()

    elif option == "3":
        pet_controller.update_pet()

    elif option == "4":
        pet_controller.delete_pet()

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

