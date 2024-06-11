import { createContext, useContext, useEffect, useState } from "react";
import { login as loginApi, logout as logoutApi } from "./auth";
import { decodeToken, getToken } from "./tokenFunctions";

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

  const login = async (credentials) => {
    try {
      const userData = await loginApi(credentials.email, credentials.password);
      console.log("Retrieved user data attempting login");
      setUser(userData);
      setIsLoggedIn(true);
      const role = userData.role;
      console.log("Login success1");
      return { role };
    } catch (error) {
      console.error("Login error", error.message);
      return { error };
    }
  };

  const logout = async () => {
    try {
      await logoutApi();
      setUser(null);
      setIsLoggedIn(false);
    } catch (error) {
      console.error("logout error", error.message);
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
