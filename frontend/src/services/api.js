import axios from "axios";

import toast from "react-hot-toast";

import {
  getToken,
  removeToken
} from "./tokenService";

const API_BASE_URL =
  "http://127.0.0.1:8000/api/v1";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json"
  },
  timeout: 10000
});

api.interceptors.request.use(
  (config) => {

    const token =
      getToken();

    if (token) {

      config.headers.Authorization =
        `Bearer ${token}`;
    }

    return config;
  },
  (error) => {

    return Promise.reject(
      error
    );
  }
);

api.interceptors.response.use(
  (response) => {

    return response;
  },
  (error) => {

    const status =
      error.response?.status;

    if (status === 401) {

      removeToken();

      if (
        window.location.pathname !==
        "/login"
      ) {

        toast.error(
          "Session expired. Please log in again."
        );

        window.location.href =
          "/login";
      }

      return Promise.reject(
        error
      );
    }

    const message =
      error.response?.data?.error ||
      error.response?.data?.detail ||
      error.message ||
      "An unexpected error occurred";

    toast.error(
      message
    );

    return Promise.reject(
      error
    );
  }
);

export default api;