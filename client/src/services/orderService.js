import api from "./apiService";

export const createOrder = async (order) => {
  const response = await api.post("/orders", order);
  return response.data;
};
