import api from "./apiService";


export const submitUserDetails = async (details) => {
  const response = await api.post("/onboarding/details", details);
  return response.data;
}
