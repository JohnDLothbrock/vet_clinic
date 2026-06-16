import api from "./api";

export async function getAuditLogs() {

  const response =
    await api.get(
      "/audit-logs"
    );

  return response.data;
}

export async function getPaginatedAuditLogs({
  page = 1,
  page_size = 10,
  action = "",
  entity = "",
  user_id = "",
  date_from = "",
  date_to = ""
}) {

  const params = {
    page,
    page_size
  };

  if (action) {

    params.action = action;
  }

  if (entity) {

    params.entity = entity;
  }

  if (user_id) {

    params.user_id = user_id;
  }

  if (date_from) {

    params.date_from = date_from;
  }

  if (date_to) {

    params.date_to = date_to;
  }

  const response =
    await api.get(
      "/audit-logs/paginated",
      {
        params
      }
    );

  return response.data;
}

export async function getAuditLogsByEntity(
  entity,
  entityId
) {

  const response =
    await api.get(
      `/audit-logs/${entity}/${entityId}`
    );

  return response.data;
}