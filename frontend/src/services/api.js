import axios from 'axios';
import toast from 'react-hot-toast';

const API_BASE_URL = 'http://127.0.0.1:8000/api/v1';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000,
});

// Request Interceptor
api.interceptors.request.use(
  (config) => {
    // You can add auth token here later
    return config;
  },
  (error) => Promise.reject(error)
);

// Response Interceptor - Global Error Handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    const message = error.response?.data?.error ||
                   error.response?.data?.detail ||
                   error.message ||
                   'An unexpected error occurred';

    toast.error(message);
    return Promise.reject(error);
  }
);

export default api;

