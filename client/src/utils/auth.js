import {
  decodeToken,
  getToken,
  removeToken,
  storeToken,
} from "./tokenFunctions";
const SERVER_URL = "http://localhost:5000";

export const loginApi = async ({ email, password }) => {
  /**
   * Logs in the user
   * @param {Object} credentials - The user's credentials
   * @param {string} credentials.email - The user's email
   * @param {string} credentials.password - The user's password
   * @returns {Object} - The user's data
   **/

  try {
    const res = await fetch(`${SERVER_URL}/api/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    const response = await res.json();

    if (res.status === 401) {
      throw new Error(response.error);
    } else if (!res.ok) {
      console.error(response.error);
      throw new Error(response.description);
    } else {
      const token = response.access_token;
      storeToken(token);
      return decodeToken(token);
    }
  } catch (error) {
    throw new Error(`Login Failed: ${error.message}`);
  }
};

export const logoutApi = async () => {
  /**
   * Logs out the user
   * @returns {void}
   **/

  const token = getToken();
  try {
    const res = await fetch(`${SERVER_URL}/api/auth/logout`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({}),
    });

    const response = await res.json();

    if (!res.ok) {
      console.error(response.error);
      throw new Error(response.description);
    }

    removeToken();
  } catch (error) {
    throw new Error(`Logout Failed: ${error.message}`);
  }
};

export const getRolesApi = async () => {
  /**
   * Retrieves the roles
   * @returns {Array} - The roles, an array of dics with id and name
   **/

  const token = getToken();
  try {
    const res = await fetch(`${SERVER_URL}/api/auth/roles`, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    });

    const response = await res.json();

    if (!res.ok) {
      console.error(response.error);
      throw new Error(response.description);
    }

    return response.roles;
  } catch (error) {
    throw new Error(`Failed To Retrieve Roles: ${error.message}`);
  }
};
