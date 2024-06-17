const SERVER_URL = "http://localhost:5000";

export const createUserApi = async ({ email, password, role }) => {
  try {
    const res = await fetch(`${SERVER_URL}/api/admin/users`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password, role }),
    });

    const response = await res.json();

    if (!res.ok) {
      throw new Error(response.error);
    } else {
      console.log("User Created");
    }
  } catch (error) {
    throw new Error(`Login failed ${response.error}`);
  }
};

export const getUsersApi = async ({ searchField, sort, page, limit }) => {
  try {
    const res = await fetch(
      `${SERVER_URL}/api/admin/users?search=${searchField}&sort=${sort}&page=${page}&limit=${limit}`
    );
    const response = await res.json();

    if (!res.ok) {
      throw new Error(response.error);
    } else {
      return response.users;
    }
  } catch (error) {
    throw new Error(`Fetch Users failed ${response.error}`);
  }
};

export const deleteUserApi = async (userId) => {
  try {
    const res = await fetch(`${SERVER_URL}/api/admin/users/${userId}`, {
      method: "DELETE",
    });

    const response = await res.json();

    if (!res.ok) {
      throw new Error(response.error);
    } else {
      console.log("User Deleted");
    }
  } catch (error) {
    throw new Error(`Delete failed ${response.error}`);
  }
};

export const updateUserApi = async ({ userId, username, email, role }) => {
  try {
    const res = await fetch(`${SERVER_URL}/api/admin/users/${userId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({username, email, role}),
    });

    const response = await res.json();

    if (!res.ok) {
      throw new Error(response.error);
    } else {
      console.log("User Updated");
    }
  } catch (error) {
    throw new Error(`Update failed ${response.error}`);
  }
};
