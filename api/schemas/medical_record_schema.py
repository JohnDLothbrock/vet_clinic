from pydantic import BaseModel


class MedicalRecordCreate(
    BaseModel
):

    pet_id: int
    visit_date: str
    weight: float
    diagnosis: str
    treatment: str
    notes: str
    created_by: int


class MedicalRecordUpdate(
    BaseModel
):

    visit_date: str
    weight: float
    diagnosis: str
    treatment: str
    notes: str


class MedicalRecordResponse(
    BaseModel
):

    id: int
    pet_id: int
    visit_date: str
    weight: float
    diagnosis: str
    treatment: str
    notes: str
    created_by: int