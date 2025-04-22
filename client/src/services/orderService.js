import api from "./apiService";

export const createOrder = async (order) => {
  const response = await api.post("/orders", order);
  return response.data;
};

export const getOrders = async ({
  searchField,
  sortBy,
  sortOrder,
  page,
  limit,
}) => {
  const response = await api.get("/orders", {
    params: { search: searchField, sortBy, sortOrder, page, limit },
  });
  return response.data.orders;
};

export const getOrderDetails = async ({
  orderId,
}) => {
  const response = await api.get("/orders/details", {
    params: { orderId },
  });
  return response.data.details;
}