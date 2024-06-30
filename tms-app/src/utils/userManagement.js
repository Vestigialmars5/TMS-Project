const SERVER_URL = "http://localhost:5000";

export const createUserApi = async ({ email, password, roleId }) => {
  /**
   * Creates a new user
   * @param {Object} userData - The user's data
   * @param {string} userData.email - The user's email
   * @param {string} userData.password - The user's password
   * @param {int} userData.roleId - The user's role id
   * @returns {void}
   **/

  try {
    const res = await fetch(`${SERVER_URL}/api/admin/users`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password, roleId }),
    });

    const response = await res.json();

    if (!res.ok) {
      throw new Error(response.error, response.description);
    } else {
      console.log("User Created");
    }
  } catch (error) {
    throw new Error(`Login failed ${error.message}`);
  }
};

// TODO: Probably remove limit
export const getUsersApi = async ({ searchField, sort, page, limit }) => {
  /**
   * Gets all users
   * @param {Object} args - The fetch filter
   * @param {string} args.searchField - The search value
   * @param {string} args.sort - The sort wanted
   * @param {int} args.page - The page number
   * @param {int} args.limit - The limit
   * @returns {Array} - The users
   **/

  try {
    const res = await fetch(
      `${SERVER_URL}/api/admin/users?search=${searchField}&sort=${sort}&page=${page}&limit=${limit}`
    );
    const response = await res.json();

    if (!res.ok) {
      throw new Error(response.error, response.description);
    } else {
      return response.users;
    }
  } catch (error) {
    throw new Error(`Fetch Users failed ${error.message}`);
  }
};

export const deleteUserApi = async (userId) => {
  /**
   * Deletes a user
   * @param {int} userId - The user's id
   * @returns {void}
   **/

  try {
    const res = await fetch(`${SERVER_URL}/api/admin/users/${userId}`, {
      method: "DELETE",
    });

    const response = await res.json();

    if (!res.ok) {
      throw new Error(response.error, response.description);
    } else {
      console.log("User Deleted");
    }
  } catch (error) {
    throw new Error(`Delete failed ${error.message}`);
  }
};

export const updateUserApi = async ({ userId, username, email, roleId }) => {
  /**
   * Updates a user
   * @param {Object} userData - The user's new data
   * @param {int} userData.userId - The user's id
   * @param {string} userData.username - The user's username
   * @param {string} userData.email - The user's email
   * @param {int} userData.roleId - The user's role id
   * @returns {void}
   **/

  try {
    const res = await fetch(`${SERVER_URL}/api/admin/users/${userId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, email, roleId }),
    });

    const response = await res.json();

    if (!res.ok) {
      throw new Error(response.error, response.description);
    } else {
      console.log("User Updated");
    }
  } catch (error) {
    throw new Error(`Update failed ${error.message}`);
  }
};
