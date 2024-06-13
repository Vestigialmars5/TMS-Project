import { decodeToken, getToken, removeToken, storeToken } from "./tokenFunctions";
const SERVER_URL = "http://localhost:5000";

// Move login logic here
export const login = async ({ email, password }) => {
  console.log("inside the login async");
  try {
    const res = await fetch(`${SERVER_URL}/api/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    const response = await res.json();

    if (!res.ok) {
      throw new Error(response.error);
    } else {
      const token = response.access_token;
      storeToken(token);
      return decodeToken(token);
    }
  } catch (error) {
    throw new Error(`Login failed ${response.error}`);
  }
};

// TODO: Move logout logic here
export const logout = async () => {
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

    if (!res.ok) {
      console.error("Logout failed:", res.status);
      throw new Error("Logout failed");
    }

    removeToken();

  } catch (error) {
    throw new Error("Error Logging out:", error);
  }
};
