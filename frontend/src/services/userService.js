import api from "./api";

export async function getUsers() {

  const response =
    await api.get(
      "/users"
    );

  return response.data;
}

export async function createUser(
  userData
) {

  const response =
    await api.post(
      "/users",
      userData
    );

  return response.data;
}

export async function updateUserRole(
  userId,
  roleId
) {

  const response =
    await api.put(
      `/users/${userId}/role`,
      {
        role_id: roleId
      }
    );

  return response.data;
}

export async function updateUserActive(
  userId,
  active
) {

  const response =
    await api.put(
      `/users/${userId}/active`,
      {
        active
      }
    );

  return response.data;
}

export async function changeMyPassword(
  passwordData
) {

  const response =
    await api.put(
      "/users/me/change-password",
      passwordData
    );

  return response.data;
}