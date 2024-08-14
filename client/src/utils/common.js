import { getToken } from "./tokenFunctions";
const SERVER_URL = "http://localhost:5000";

export const getRolesApi = async () => {
  /**
   * Retrieves the roles
   * @returns {Array} - The roles, an array of dics with id and name
   **/

  const token = getToken();
  try {
    const res = await fetch(`${SERVER_URL}/api/common/roles`, {
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
