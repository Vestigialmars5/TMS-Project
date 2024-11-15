import api from "./apiService";

export const submitUserDetails = async (details) => {
  const response = await api.post("/onboarding/details", details);
  return response.data;
};

export const getCurrentStep = async () => {
  const response = await api.get("/onboarding/step", {});
  return response.data.step;
}

export const submitRoleDetails = async ({ roleId, details }) => {
  const response = await api.post(`/onboarding/${roleId}`, details);
  return response.data
};
