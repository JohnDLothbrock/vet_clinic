import api from "./api";

export async function getMedicalRecords() {

  const response =
    await api.get(
      "/medical-records"
    );

  return response.data;
}

export async function getMedicalRecordsByPet(
  petId
) {

  const response =
    await api.get(
      `/medical-records/pet/${petId}`
    );

  return response.data;
}

export async function createMedicalRecord(
  medicalRecordData
) {

  const response =
    await api.post(
      "/medical-records",
      medicalRecordData
    );

  return response.data;
}

export async function updateMedicalRecord(
  medicalRecordId,
  medicalRecordData
) {

  const response =
    await api.put(
      `/medical-records/${medicalRecordId}`,
      medicalRecordData
    );

  return response.data;
}

export async function deleteMedicalRecord(
  medicalRecordId
) {

  const response =
    await api.delete(
      `/medical-records/${medicalRecordId}`
    );

  return response.data;
}