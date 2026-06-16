import api from "./api";

export async function getOwners() {

  const response =
    await api.get(
      "/owners"
    );

  return response.data;
}

export async function getPaginatedOwners({
  page = 1,
  page_size = 10,
  search = ""
}) {

  const params = {
    page,
    page_size
  };

  if (search) {

    params.search = search;
  }

  const response =
    await api.get(
      "/owners/paginated",
      {
        params
      }
    );

  return response.data;
}

export async function searchOwners(
  name
) {

  const response =
    await api.get(
      `/owners/search/${name}`
    );

  return response.data;
}

export async function createOwner(
  ownerData
) {

  const response =
    await api.post(
      "/owners",
      ownerData
    );

  return response.data;
}

export async function updateOwner(
  ownerId,
  ownerData
) {

  const response =
    await api.put(
      `/owners/${ownerId}`,
      ownerData
    );

  return response.data;
}

export async function deleteOwner(
  ownerId
) {

  const response =
    await api.delete(
      `/owners/${ownerId}`
    );

  return response.data;
}