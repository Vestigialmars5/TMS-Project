import api from "./apiService";

export const getRoles = async () => {
  const response = await api.get("/roles");
  return response.data.roles;
};

export const getUsers = async ({
  searchField,
  sortBy,
  sortOrder,
  page,
  limit,
}) => {
  const response = await api.get("/users", {
    params: { search: searchField, sortBy, sortOrder, page, limit },
  });
  return response.data.users;
};

export const createUser = async (user) => {
  await api.post(`/users`, user);
};

export const deleteUser = async (userId) => {
  await api.delete(`/users/${userId}`, {});
};

export const updateUser = async ({ userId, email, roleId }) => {
  const response = await api.put(`/users/${userId}`, { email, roleId });
  return response.data;
};
