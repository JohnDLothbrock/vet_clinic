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

    <div className="medical-record-card clinical-record-card">

      <div className="record-main clinical-record-main">

        <div className="record-avatar medical-record-avatar">
          🩺
        </div>

        <div className="clinical-record-content">

          <div className="clinical-record-header">

            <div>

              <h3>
                {pet
                  ? `${pet.name} (${pet.owner_name})`
                  : `Pet ID: ${medicalRecord.pet_id}`}
              </h3>

              <p className="clinical-record-date">
                {medicalRecord.visit_date}
              </p>

            </div>

            <span className="medical-record-badge">
              Clinical Record
            </span>

          </div>

          <div className="medical-record-meta">

            <span>
              <strong>
                Weight:
              </strong>
              {" "}
              {medicalRecord.weight}
            </span>

            <span>
              <strong>
                Created By:
              </strong>
              {" "}
              User {medicalRecord.created_by}
            </span>

          </div>

          <div className="clinical-section">

            <h4>
              Diagnosis
            </h4>

            <p>
              {medicalRecord.diagnosis}
            </p>

          </div>

          <div className="clinical-section">

            <h4>
              Treatment
            </h4>

            <p>
              {medicalRecord.treatment}
            </p>

          </div>

          {medicalRecord.notes && (

            <div className="clinical-section">

              <h4>
                Notes
              </h4>

              <p>
                {medicalRecord.notes}
              </p>

            </div>

          )}

        </div>

      </div>

      {showActions && (

        <div className="button-group record-actions">

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
              className="small-button"
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
              className="delete-button small-button"
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