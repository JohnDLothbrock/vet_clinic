import api from "./api";

import {
  saveToken,
  removeToken,
  getUserFromToken
} from "./tokenService";

export async function login(
  username,
  password
) {

  const response =
    await api.post(
      "/auth/login",
      {
        username,
        password
      }
    );

  const token =
    response.data.access_token;

  saveToken(
    token
  );

  return getUserFromToken();
}

export async function requestPasswordReset(
  email
) {

  const response =
    await api.post(
      "/auth/forgot-password",
      {
        email
      }
    );

  return response.data;
}

export async function resetPassword(
  token,
  newPassword
) {

  const response =
    await api.post(
      "/auth/reset-password",
      {
        token,
        new_password: newPassword
      }
    );

  return response.data;
}

export function logout() {

  removeToken();
}

export function getCurrentUser() {

  return getUserFromToken();
}