class MedicalRecord:

    def __init__(
            self,
            pet_id,
            visit_date,
            weight,
            diagnosis,
            treatment,
            notes,
            created_by,
            medical_record_id=None
    ):

        self.id = medical_record_id
        self.pet_id = pet_id
        self.visit_date = visit_date
        self.weight = weight
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.notes = notes
        self.created_by = created_by