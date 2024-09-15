import api from "./apiService";

export const login = async (credentials) => {
  const response = await api.post("/auth/login", credentials);
  return response.data;
};

export const logout = async () => {
  try {
    await api.post("/auth/logout");
  } catch (error) {
    console.error(error);
    throw new Error(error.response?.data?.description || "Logout failed");
  }
};
