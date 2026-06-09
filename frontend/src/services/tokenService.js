const TOKEN_KEY = "vet_clinic_access_token";

export function saveToken(token) {

  localStorage.setItem(
    TOKEN_KEY,
    token
  );
}

export function getToken() {

  return localStorage.getItem(
    TOKEN_KEY
  );
}

export function removeToken() {

  localStorage.removeItem(
    TOKEN_KEY
  );
}

export function getUserFromToken() {

  const token = getToken();

  if (!token) {

    return null;
  }

  try {

    const payloadBase64 =
      token.split(".")[1];

    const decodedPayload =
      JSON.parse(
        atob(payloadBase64)
      );

    return decodedPayload;

  } catch (error) {

    console.error(
      "Invalid token:",
      error
    );

    removeToken();

    return null;
  }
}

export function isTokenExpired() {

  const user =
    getUserFromToken();

  if (!user || !user.exp) {

    return true;
  }

  const currentTime =
    Math.floor(
      Date.now() / 1000
    );

  return user.exp < currentTime;
}

export function isAuthenticated() {

  const token = getToken();

  if (!token) {

    return false;
  }

  if (isTokenExpired()) {

    removeToken();

    return false;
  }

  return true;
}

export function getUserRoleId() {

  const user =
    getUserFromToken();

  return user?.role_id || null;
}

export function getUsername() {

  const user =
    getUserFromToken();

  return user?.sub || "";
}