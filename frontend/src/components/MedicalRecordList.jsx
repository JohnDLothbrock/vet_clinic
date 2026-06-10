import MedicalRecordItem from "./MedicalRecordItem";

function MedicalRecordList({

  medicalRecords,
  pets,
  editMedicalRecord,
  deleteMedicalRecord,
  deletingId

}) {

  if (medicalRecords.length === 0) {

    return (

      <div className="empty-state">

        <div className="empty-state-icon medical-empty-icon">
          🩺
        </div>

        <h3>
          No medical records found
        </h3>

        <p>
          Create a new medical record or clear the pet filter.
        </p>

      </div>
    );
  }

  return (

    <div className="medical-record-list">

      {medicalRecords.map(
        (medicalRecord) => (

          <MedicalRecordItem
            key={medicalRecord.id}
            medicalRecord={medicalRecord}
            pets={pets}
            editMedicalRecord={
              editMedicalRecord
            }
            deleteMedicalRecord={
              deleteMedicalRecord
            }
            deletingId={deletingId}
          />

        )
      )}

    </div>
  );
}

export default MedicalRecordList;