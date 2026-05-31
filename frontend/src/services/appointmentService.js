const API_URL =
  "http://127.0.0.1:8000/api/v1/appointments";

export async function getAppointments() {

  const response = await fetch(
    `${API_URL}/with-pet`
  );

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error || "Failed to load appointments."
    );
  }

  return data;
}

export async function createAppointment(
  appointmentData
) {

  const response = await fetch(
    API_URL,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(
        appointmentData
      )
    }
  );

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error || "Failed to create appointment."
    );
  }

  return data;
}

export async function updateAppointment(
  appointmentId,
  appointmentData
) {

  const response =
    await fetch(
      `${API_URL}/${appointmentId}`,
      {
        method: "PUT",
        headers: {
          "Content-Type":
            "application/json"
        },
        body: JSON.stringify(
          appointmentData
        )
      }
    );

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error || "Failed to update appointment."
    );
  }

  return data;
}

export async function deleteAppointment(
  appointmentId
) {

  const response =
    await fetch(
      `${API_URL}/${appointmentId}`,
      {
        method: "DELETE"
      }
    );

  const data =
    await response.json();

  if (!response.ok) {

    throw new Error(
      data.error || "Failed to delete appointment."
    );
  }

  return data;
}
