const API_URL =
  "http://127.0.0.1:8000/api/v1/dashboard";

export async function getDashboardData() {

  const response =
    await fetch(API_URL);

  return await response.json();
}