import { createContext, useContext, useEffect, useState } from "react";
import { loginApi, logoutApi, getRolesApi } from "../utils/auth";
import { decodeToken, getToken } from "../utils/tokenFunctions";
import { useNavigate } from "react-router-dom";
import { navigateBasedOnRole } from "../utils/navigation";

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isOnboarded, setIsOnboarded] = useState(false);
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [roles, setRoles] = useState([]);

  const navigate = useNavigate();

  // On mount check for token, this is if still logged in
  useEffect(() => {
    const token = getToken();
    if (token) {
      const decoded = decodeToken(token);
      setUser(decoded);
      setIsLoggedIn(true);
      if (!decoded.isOnboardingCompleted) {
        setIsOnboarded(false);
        navigate("/onboarding");
      } else {
        setIsOnboarded(true);
      }
    }

    const delayTimeout = setTimeout(() => {
      setLoading(false);
    }, 0); // Modify timeout for smoothness

    return () => clearTimeout(delayTimeout);
  }, []);

  const updateUser = (userData) => {
    setUser(userData);
  };

  const login = async (credentials) => {
    try {
      const userData = await loginApi(credentials.email, credentials.password);
      const roleName = userData.roleName;
      const isOnboardingCompleted = userData.isOnboardingCompleted;
      setUser(userData);
      setIsLoggedIn(true);
      setIsOnboarded(isOnboardingCompleted);
      if (!isOnboardingCompleted) {
        navigate("/onboarding");
      } else {
        navigateBasedOnRole(roleName, navigate);
      }
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

  const getRoles = async () => {
    try {
      const roles = await getRolesApi();
      setRoles(roles);
    } catch (error) {
      console.error("Error retrieving roles", error.message);
    }
  };

  const isAuthorized = (requiredRoleId) => {
    return user && user.roleId === requiredRoleId;
  };

  return (
    <AuthContext.Provider
      value={{
        isLoggedIn,
        isOnboarded,
        user,
        loading,
        roles,
        updateUser,
        login,
        logout,
        isAuthorized,
        getRoles,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};
