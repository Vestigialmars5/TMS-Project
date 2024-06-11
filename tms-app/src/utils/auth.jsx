import { createContext, useContext, useEffect, useState } from "react";
import { decodeToken, getToken, removeToken, storeToken } from "./tokenFunctions";

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // On mount check for token, this is if still logged in
  useEffect(() => {
    const token = getToken();
    if (token) {
      console.log("found token");
      const decoded = decodeToken(token);
      setUser({ email: decoded.email, role: decoded.role });
      setIsLoggedIn(true);
    }

    const delayTimeout = setTimeout(() => {
      setLoading(false);
    }, 700);

    return () => clearTimeout(delayTimeout);
  }, []);

  // Move login logic here
  const login = async ({ email, password }) => {
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
        const token = response.access_token;
        const decoded = decodeToken(token);
        console.log("good Response token, decoded", token, decoded);
        setUser({ email: decoded.email, role: decoded.role });
        setIsLoggedIn(true);
        console.log("Login success:");
        storeToken(token);
        console.log("stored");
        const role = decoded.role;
        return {role};
      }
    } catch (error) {
      console.error("Login error:", error.message);
      return {error};
    }
  };

  // TODO: Move logout logic here
  const logout = async () => {
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

      if (res.ok) {
        removeToken(token);
        setUser(null);
        setIsLoggedIn(false);
        return null;
      } else {
        console.error("Logout failed:", res.status);
        throw new Error("Logout failed");
      }
    } catch (error) {
      console.error("Error Logging out:", error);
      throw new Error("Error Logging out:", error);
    }
  };

  const isAuthorized = (requiredRole) => {
    return user && user.role === requiredRole;
  };

  return (
    <AuthContext.Provider
      value={{ isLoggedIn, user, loading, login, logout, isAuthorized }}
    >
      {children}
    </AuthContext.Provider>
  );
};
