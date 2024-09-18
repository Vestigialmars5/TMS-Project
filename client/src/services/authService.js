import api from "./apiService";

export const login = async (credentials) => {
  try {
    const response = await api.post("/auth/login", credentials);
    // Add alert here
    return response.data;
  } catch (error) {
    // Add alert here
    throw error;
  }
};

export const logout = async () => {
  try {
    await api.post("/auth/logout", {});
    // Add alert here
  } catch (error) {
    // Add alert here
    throw error;
  }
};
