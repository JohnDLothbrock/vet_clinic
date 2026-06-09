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

export function logout() {

  removeToken();
}

export function getCurrentUser() {

  return getUserFromToken();
}