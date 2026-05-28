const API_URL = "http://127.0.0.1:8000/api/v1/pets";

export async function getPets() {

  const response = await fetch(API_URL);

  return await response.json();
}

export async function createPet(petData) {

  await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(petData)
  });
}

export async function updatePet(
  petId,
  petData
) {

  await fetch(
    `${API_URL}/${petId}`,
    {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(petData)
    }
  );
}

export async function deletePet(
  petId
) {

  await fetch(
    `${API_URL}/${petId}`,
    {
      method: "DELETE"
    }
  );
}