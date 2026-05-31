const API_URL =
  "http://127.0.0.1:8000/api/v1/appointments";

export async function getAppointments() {

  const response = await fetch(
    `${API_URL}/with-pet`
  );

  return await response.json();
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

  console.log(
    "CREATE RESPONSE:",
    data
  );

  if (!response.ok) {

    throw new Error(
      JSON.stringify(data)
    );
  }

  return data;
}

export async function updateAppointment(
  appointmentId,
  appointmentData
) {

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
}

export async function deleteAppointment(
  appointmentId
) {

  await fetch(
    `${API_URL}/${appointmentId}`,
    {
      method: "DELETE"
    }
  );
}