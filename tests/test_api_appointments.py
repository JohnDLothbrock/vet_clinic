from fastapi.testclient import TestClient

from main_api import app

client = TestClient(app)


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