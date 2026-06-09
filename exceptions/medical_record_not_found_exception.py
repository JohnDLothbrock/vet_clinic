from exceptions.application_exception import (
    ApplicationException
)


class MedicalRecordNotFoundException(
    ApplicationException
):

    def __init__(
            self,
            medical_record_id: int
    ):

        super().__init__(
            f"Medical record with ID {medical_record_id} not found",
            404
        )