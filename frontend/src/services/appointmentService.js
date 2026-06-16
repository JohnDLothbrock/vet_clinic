import api from "./api";

export async function getAppointments() {

  const response =
    await api.get(
      "/appointments/with-pet"
    );

  return response.data;
}

export async function getPaginatedAppointments({
  page = 1,
  page_size = 10,
  search = "",
  pet_id = "",
  date_from = "",
  date_to = ""
}) {

  const params = {
    page,
    page_size
  };

  if (search) {

    params.search = search;
  }

  if (pet_id) {

    params.pet_id = pet_id;
  }

  if (date_from) {

    params.date_from = date_from;
  }

  if (date_to) {

    params.date_to = date_to;
  }

  const response =
    await api.get(
      "/appointments/paginated",
      {
        params
      }
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