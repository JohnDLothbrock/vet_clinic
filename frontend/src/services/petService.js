const API_URL =
  "http://127.0.0.1:8000/api/v1/pets";

export async function getPets() {

  const response =
    await fetch(API_URL);

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error ||
      "Failed to load pets."
    );
  }

  return data;
}

export async function createPet(
  petData
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
          petData
        )
      }
    );

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error ||
      "Failed to create pet."
    );
  }

  return data;
}

export async function updatePet(
  petId,
  petData
) {

  const response =
    await fetch(
      `${API_URL}/${petId}`,
      {
        method: "PUT",
        headers: {
          "Content-Type":
            "application/json"
        },
        body: JSON.stringify(
          petData
        )
      }
    );

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error ||
      "Failed to update pet."
    );
  }

  return data;
}

export async function deletePet(
  petId
) {

  const response =
    await fetch(
      `${API_URL}/${petId}`,
      {
        method: "DELETE"
      }
    );

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error ||
      "Failed to delete pet."
    );
  }

  return data;
}

export async function searchPets(
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
      "Failed to search pets."
    );
  }

  return data;
}

export async function getPetsWithOwner() {

  const response =
    await fetch(
      `${API_URL}/with-owner`
    );

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error ||
      "Failed to load pets."
    );
  }

  return data;
}