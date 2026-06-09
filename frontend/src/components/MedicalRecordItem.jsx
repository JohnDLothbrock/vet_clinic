import {
  canEditMedicalRecord,
  canDeleteMedicalRecord
} from "../services/permissionService";

function MedicalRecordItem({

  medicalRecord,
  pets,
  editMedicalRecord,
  deleteMedicalRecord,
  deletingId

}) {

  const pet =
    pets.find(
      (item) =>
        item.id === medicalRecord.pet_id
    );

  const showActions =
    canEditMedicalRecord() ||
    canDeleteMedicalRecord();

  return (

    <div className="medical-record-card">

      <div>

        <h3>
          {pet
            ? `${pet.name} (${pet.owner_name})`
            : `Pet ID: ${medicalRecord.pet_id}`}
        </h3>

        <p>
          <strong>
            Visit Date:
          </strong>
          {" "}
          {medicalRecord.visit_date}
        </p>

        <p>
          <strong>
            Weight:
          </strong>
          {" "}
          {medicalRecord.weight}
        </p>

        <p>
          <strong>
            Diagnosis:
          </strong>
          {" "}
          {medicalRecord.diagnosis}
        </p>

        <p>
          <strong>
            Treatment:
          </strong>
          {" "}
          {medicalRecord.treatment}
        </p>

        <p>
          <strong>
            Notes:
          </strong>
          {" "}
          {medicalRecord.notes}
        </p>

        <p>
          <strong>
            Created By User ID:
          </strong>
          {" "}
          {medicalRecord.created_by}
        </p>

      </div>

      {showActions && (

        <div className="button-group">

          {canEditMedicalRecord() && (

            <button
              onClick={() =>
                editMedicalRecord(
                  medicalRecord
                )
              }
              disabled={
                deletingId === medicalRecord.id
              }
            >
              Edit
            </button>

          )}

          {canDeleteMedicalRecord() && (

            <button
              onClick={() =>
                deleteMedicalRecord(
                  medicalRecord.id
                )
              }
              disabled={
                deletingId === medicalRecord.id
              }
              className="delete-button"
            >
              {deletingId === medicalRecord.id
                ? "Deleting..."
                : "Delete"}
            </button>

          )}

        </div>

      )}

    </div>
  );
}

export default MedicalRecordItem;