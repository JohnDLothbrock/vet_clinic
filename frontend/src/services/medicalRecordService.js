import api from "./api";

export async function getMedicalRecords() {

  const response =
    await api.get(
      "/medical-records"
    );

  return response.data;
}

export async function getPaginatedMedicalRecords({
  page = 1,
  page_size = 10,
  search = "",
  pet_id = "",
  date_from = "",
  date_to = ""
}) {

  const params = {
    page,
    page_size
  };

  if (search) {

    params.search = search;
  }

  if (pet_id) {

    params.pet_id = pet_id;
  }

  if (date_from) {

    params.date_from = date_from;
  }

  if (date_to) {

    params.date_to = date_to;
  }

  const response =
    await api.get(
      "/medical-records/paginated",
      {
        params
      }
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