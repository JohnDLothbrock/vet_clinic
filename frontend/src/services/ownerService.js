const API_URL =
  "http://127.0.0.1:8000/api/v1/owners";

export async function getOwners() {

  const response =
    await fetch(API_URL);

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error ||
      "Failed to load owners."
    );
  }

  return data;
}

export async function searchOwners(
  name
) {

  const response =
    await fetch(
      `${API_URL}/search/${name}`
    );

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error ||
      "Failed to search owners."
    );
  }

  return data;
}

export async function createOwner(
  ownerData
) {

  const response =
    await fetch(
      API_URL,
      {
        method: "POST",
        headers: {
          "Content-Type":
            "application/json"
        },
        body: JSON.stringify(
          ownerData
        )
      }
    );

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error ||
      "Failed to create owner."
    );
  }

  return data;
}

export async function updateOwner(
  ownerId,
  ownerData
) {

  const response =
    await fetch(
      `${API_URL}/${ownerId}`,
      {
        method: "PUT",
        headers: {
          "Content-Type":
            "application/json"
        },
        body: JSON.stringify(
          ownerData
        )
      }
    );

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error ||
      "Failed to update owner."
    );
  }

  return data;
}

export async function deleteOwner(
  ownerId
) {

  const response =
    await fetch(
      `${API_URL}/${ownerId}`,
      {
        method: "DELETE"
      }
    );

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error ||
      "Failed to delete owner."
    );
  }

  return data;
}