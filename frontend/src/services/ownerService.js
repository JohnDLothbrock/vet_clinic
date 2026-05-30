const API_URL = "http://127.0.0.1:8000/api/v1/owners";

export async function getOwners() {

  const response = await fetch(API_URL);

  return await response.json();
}

export async function createOwner(ownerData) {

  await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(ownerData)
  });
}

export async function updateOwner(
  ownerId,
  ownerData
) {

  await fetch(
    `${API_URL}/${ownerId}`,
    {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(ownerData)
    }
  );
}

export async function deleteOwner(
  ownerId
) {

  await fetch(
    `${API_URL}/${ownerId}`,
    {
      method: "DELETE"
    }
  );
}