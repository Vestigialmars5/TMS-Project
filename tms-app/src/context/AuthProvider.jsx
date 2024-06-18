import { createContext, useContext, useEffect, useState } from "react";
import { login as loginApi, logout as logoutApi } from "../utils/auth";
import { decodeToken, getToken } from "../utils/tokenFunctions";

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
      const decoded = decodeToken(token);
      setUser({ email: decoded.email, role: decoded.role });
      setIsLoggedIn(true);
    }

    const delayTimeout = setTimeout(() => {
      setLoading(false);
    }, 0); // Modify timeout for smoothness

    return () => clearTimeout(delayTimeout);
  }, []);

  const login = async (credentials) => {
    try {
      const userData = await loginApi(credentials.email, credentials.password);
      setUser(userData);
      setIsLoggedIn(true);
      const role = userData.role;
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
