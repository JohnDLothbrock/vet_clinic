from exceptions.pet_not_found_exception import (
    PetNotFoundException
)

from utils.logger import logger

from validators.medical_record_validator import (
    MedicalRecordValidator
)


class MedicalRecordService:

    def __init__(
            self,
            medical_record_repository,
            pet_service
    ):

        self.medical_record_repository = (
            medical_record_repository
        )

        self.pet_service = (
            pet_service
        )

    def create_medical_record(
            self,
            medical_record
    ):

        pet = (
            self.pet_service.get_pet_by_id(
                medical_record.pet_id
            )
        )

        if not pet:

            raise PetNotFoundException(
                medical_record.pet_id
            )

        MedicalRecordValidator.validate(
            medical_record.visit_date,
            medical_record.weight,
            medical_record.diagnosis,
            medical_record.treatment
        )

        self.medical_record_repository.create(
            medical_record
        )

        logger.info(
            f"Medical record created for pet {medical_record.pet_id}"
        )

    def get_all_medical_records(self):

        return (
            self.medical_record_repository
            .get_all()
        )

    def get_medical_record_by_id(
            self,
            medical_record_id
    ):

        return (
            self.medical_record_repository
            .get_by_id(
                medical_record_id
            )
        )

    def update_medical_record(
            self,
            medical_record
    ):

        MedicalRecordValidator.validate(
            medical_record.visit_date,
            medical_record.weight,
            medical_record.diagnosis,
            medical_record.treatment
        )

        self.medical_record_repository.update(
            medical_record
        )

    def delete_medical_record(
            self,
            medical_record_id
    ):

        self.medical_record_repository.delete(
            medical_record_id
        )

    def get_medical_records_by_pet(
            self,
            pet_id
    ):

        return (
            self.medical_record_repository
            .get_by_pet_id(
                pet_id
            )
        )