import api from "./apiService";
import { showAlert } from "../store/actions/alertsActions";


export const submitUserDetails = async (details) => {
  try {
    const response = await api.post("/onboarding/details", details);
    showAlert("Details Submitted Successfully", "success");
    return response.data;
  } catch (error) {
    const message = error.response?.data?.description || error.response?.data?.error || "An Unknown Error Occurred";
    showAlert(`Error Submitting Details: ${message}`, "danger");
    console.error(error.response?.data?.error || "An Unknown Error Occurred");
    throw error
  }
};
