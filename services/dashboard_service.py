class DashboardService:

    def __init__(
            self,
            owner_service,
            pet_service,
            appointment_service
    ):

        self.owner_service = owner_service
        self.pet_service = pet_service
        self.appointment_service = (
            appointment_service
        )

    def get_dashboard_data(self):

        owners = (
            self.owner_service.get_all_owners()
        )

        pets = (
            self.pet_service.get_all_pets()
        )

        appointments = (
            self.appointment_service
            .get_all_appointments()
        )

        return {

            "total_owners":
                len(owners),

            "total_pets":
                len(pets),

            "total_appointments":
                len(appointments)
        }