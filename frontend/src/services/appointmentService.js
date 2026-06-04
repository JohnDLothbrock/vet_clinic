import api from "./api";

export async function getAppointments() {

  const response =
    await api.get(
      "/appointments/with-pet"
    );

  return response.data;
}

export async function createAppointment(
  appointmentData
) {

  const response =
    await api.post(
      "/appointments",
      appointmentData
    );

  return response.data;
}

export async function updateAppointment(
  appointmentId,
  appointmentData
) {

  const response =
    await api.put(
      `/appointments/${appointmentId}`,
      appointmentData
    );

  return response.data;
}

export async function deleteAppointment(
  appointmentId
) {

  const response =
    await api.delete(
      `/appointments/${appointmentId}`
    );

  return response.data;
}