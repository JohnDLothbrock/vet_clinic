import api from "./api";

export async function getPets() {

  const response =
    await api.get(
      "/pets"
    );

  return response.data;
}

export async function createPet(
  petData
) {

  const response =
    await api.post(
      "/pets",
      petData
    );

  return response.data;
}

export async function updatePet(
  petId,
  petData
) {

  const response =
    await api.put(
      `/pets/${petId}`,
      petData
    );

  return response.data;
}

export async function deletePet(
  petId
) {

  const response =
    await api.delete(
      `/pets/${petId}`
    );

  return response.data;
}

export async function searchPets(
  name
) {

  const response =
    await api.get(
      `/pets/search/${name}`
    );

  return response.data;
}

export async function getPetsWithOwner() {

  const response =
    await api.get(
      "/pets/with-owner"
    );

  return response.data;
}