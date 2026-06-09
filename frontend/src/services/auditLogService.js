import api from "./api";

export async function getAuditLogs() {

  const response =
    await api.get(
      "/audit-logs"
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