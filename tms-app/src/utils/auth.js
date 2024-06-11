import { decodeToken, getToken, removeToken, storeToken } from "./tokenFunctions";

// Move login logic here
export const login = async ({ email, password }) => {
  console.log("inside the login async");
  try {
    const res = await fetch("http://localhost:5000/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    const response = await res.json();
    console.log("got response,", response);

    if (!res.ok) {
      console.error("response bad");
      throw new Error(response.error);
    } else {
      console.log("response good");
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
    const res = await fetch("http://localhost:5000/auth/logout", {
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
