import api from "./apiService";

export const submitUserDetails = async (details) => {
  const response = await api.post("/onboarding/details", details);
  return response.data;
};

export const getCurrentStep = async () => {
  const response = await api.get("/onboarding/step", {});
  return response.data.step;
}

export const submitRoleDetails = async (details) => {
  const response = await api.post(`/onboarding/role`, details);
  return response.data
};
