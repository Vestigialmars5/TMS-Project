import axios from "axios";
import tokenService from "./tokenService";
import {store} from "../store";
import {forceLogout} from "../store/slices/authSlice";

const baseURL = "http://localhost:5000/api";

const api = axios.create({
  baseURL: baseURL,
});

api.interceptors.request.use(async (config) => {
  const accessToken = tokenService.getAccessToken();
  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }
  return config;
});

api.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const originalRequest = error.config;
    const isUnauthorized = error.response.status === 401;
    const isNotInvalidLoginCredentials = error.response.data.error !== "Invalid Login Credentials";
    const hasNotBeenRetried = !originalRequest._retry;
    if (isUnauthorized && isNotInvalidLoginCredentials && hasNotBeenRetried) {
      originalRequest._retry = true;

      try {
        const refreshToken = tokenService.getRefreshToken();
        const response = await axios.post(
          `${baseURL}/auth/refresh`,
          {},
          {
            headers: {
              Authorization: `Bearer ${refreshToken}`,
            },
          }
        );
        const {accessToken} = response.data;
        tokenService.setAccessToken(accessToken);
        originalRequest.headers.Authorization = `Bearer ${accessToken}`;
        return api(originalRequest);
      } catch (refreshError) {
        store.dispatch(forceLogout());
        return Promise.reject(refreshError);
      }
    }
    return Promise.reject(error);
  }
);

export default api;
