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
      <p>
        No medical records found.
      </p>
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