from exceptions.pet_not_found_exception import (
    PetNotFoundException
)

from exceptions.medical_record_not_found_exception import (
    MedicalRecordNotFoundException
)

from utils.logger import logger

from validators.medical_record_validator import (
    MedicalRecordValidator
)


class MedicalRecordService:

    def __init__(
            self,
            medical_record_repository,
            pet_service,
            audit_log_service=None
    ):

        self.medical_record_repository = (
            medical_record_repository
        )

        self.pet_service = (
            pet_service
        )

        self.audit_log_service = (
            audit_log_service
        )

    def create_medical_record(
            self,
            medical_record,
            user_id=None
    ):

        pet = (
            self.pet_service.get_pet_by_id(
                medical_record.pet_id
            )
        )

        if not pet:

            logger.warning(
                f"Pet ID {medical_record.pet_id} not found"
            )

            raise PetNotFoundException(
                medical_record.pet_id
            )

        MedicalRecordValidator.validate(
            medical_record.visit_date,
            medical_record.weight,
            medical_record.diagnosis,
            medical_record.treatment
        )

        medical_record_id = (
            self.medical_record_repository.create(
                medical_record
            )
        )

        if self.audit_log_service and user_id:

            self.audit_log_service.create_audit_log(
                user_id=user_id,
                action="CREATE",
                entity="MedicalRecord",
                entity_id=medical_record_id
            )

        logger.info(
            (
                f"Medical record created: "
                f"{medical_record_id} "
                f"for pet {medical_record.pet_id}"
            )
        )

        return medical_record_id

    def get_all_medical_records(self):

        return (
            self.medical_record_repository
            .get_all()
        )

    def get_medical_record_by_id(
            self,
            medical_record_id
    ):

        medical_record = (
            self.medical_record_repository
            .get_by_id(
                medical_record_id
            )
        )

        if not medical_record:

            logger.warning(
                f"Medical record ID {medical_record_id} not found"
            )

            raise MedicalRecordNotFoundException(
                medical_record_id
            )

        return medical_record

    def update_medical_record(
            self,
            medical_record,
            user_id=None
    ):

        existing_medical_record = (
            self.medical_record_repository
            .get_by_id(
                medical_record.id
            )
        )

        if not existing_medical_record:

            logger.warning(
                f"Medical record ID {medical_record.id} not found"
            )

            raise MedicalRecordNotFoundException(
                medical_record.id
            )

        MedicalRecordValidator.validate(
            medical_record.visit_date,
            medical_record.weight,
            medical_record.diagnosis,
            medical_record.treatment
        )

        self.medical_record_repository.update(
            medical_record
        )

        if self.audit_log_service and user_id:

            self.audit_log_service.create_audit_log(
                user_id=user_id,
                action="UPDATE",
                entity="MedicalRecord",
                entity_id=medical_record.id
            )

        logger.info(
            f"Medical record updated: {medical_record.id}"
        )

        return medical_record.id

    def delete_medical_record(
            self,
            medical_record_id,
            user_id=None
    ):

        existing_medical_record = (
            self.medical_record_repository
            .get_by_id(
                medical_record_id
            )
        )

        if not existing_medical_record:

            logger.warning(
                f"Medical record ID {medical_record_id} not found"
            )

            raise MedicalRecordNotFoundException(
                medical_record_id
            )

        self.medical_record_repository.delete(
            medical_record_id
        )

        if self.audit_log_service and user_id:

            self.audit_log_service.create_audit_log(
                user_id=user_id,
                action="DELETE",
                entity="MedicalRecord",
                entity_id=medical_record_id
            )

        logger.info(
            f"Medical record deleted: {medical_record_id}"
        )

        return medical_record_id

    def get_medical_records_by_pet(
            self,
            pet_id
    ):

        pet = (
            self.pet_service.get_pet_by_id(
                pet_id
            )
        )

        if not pet:

            logger.warning(
                f"Pet ID {pet_id} not found"
            )

            raise PetNotFoundException(
                pet_id
            )

        return (
            self.medical_record_repository
            .get_by_pet_id(
                pet_id
            )
        )