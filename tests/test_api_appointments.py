from datetime import datetime
from types import SimpleNamespace

from fastapi.testclient import TestClient

from main_api import app

from app.dependencies import (
    get_appointment_service
)

from auth.current_user import (
    require_authenticated_user,
    require_admin
)


client = TestClient(app)


class FakeAppointmentService:

    def get_all_appointments(self):

        return [
            SimpleNamespace(
                id=1,
                pet_id=1,
                appointment_date=datetime.now(),
                reason="General checkup"
            )
        ]

    def get_all_appointments_with_pet(self):

        return [
            {
                "id": 1,
                "pet_id": 1,
                "pet_name": "Max",
                "appointment_date": datetime.now(),
                "reason": "General checkup"
            }
        ]


def fake_current_user():

    return {
        "user_id": 1,
        "sub": "admin",
        "role_id": 1
    }


app.dependency_overrides[
    get_appointment_service
] = lambda: FakeAppointmentService()

app.dependency_overrides[
    require_authenticated_user
] = fake_current_user

app.dependency_overrides[
    require_admin
] = fake_current_user


def test_get_appointments():

    response = client.get(
        "/api/v1/appointments"
    )

    assert response.status_code == 200


def test_get_appointments_with_pet():

    response = client.get(
        "/api/v1/appointments/with-pet"
    )

    assert response.status_code == 200