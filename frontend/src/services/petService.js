import api from "./api";

export async function getPets() {

  const response =
    await api.get(
      "/pets"
    );

  return response.data;
}

export async function getPaginatedPetsWithOwner({
  page = 1,
  page_size = 10,
  search = "",
  species = "",
  owner_id = ""
}) {

  const params = {
    page,
    page_size
  };

  if (search) {

    params.search = search;
  }

  if (species) {

    params.species = species;
  }

  if (owner_id) {

    params.owner_id = owner_id;
  }

  const response =
    await api.get(
      "/pets/with-owner-paginated",
      {
        params
      }
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