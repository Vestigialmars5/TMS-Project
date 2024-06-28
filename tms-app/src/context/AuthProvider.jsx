import { createContext, useContext, useEffect, useState } from "react";
import { loginApi, logoutApi, getRolesApi } from "../utils/auth";
import { decodeToken, getToken } from "../utils/tokenFunctions";
import { useNavigate } from "react-router-dom";

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

  const updateLoginStatus = (status) => {
    console.log("Updating login status", status);
    setIsLoggedIn(status);
  };

  const login = async (credentials) => {
    try {
      const userData = await loginApi(credentials.email, credentials.password);
      const roleName = userData.roleName;
      const isOnboardingNeeded = userData.onboardingCompleted;
      console.log("onboarding", isOnboardingNeeded);
      setUser(userData);
      setIsLoggedIn(true);
      setIsOnboarded(isOnboardingNeeded);
      if (!isOnboardingNeeded) {
        console.log("Onboarding needed");
        navigate("/onboarding");
      } else {
        console.log("Onboarding not needed");
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
    console.log("User role", user.roleId);
    console.log("Required role", requiredRoleId);
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
        updateLoginStatus,
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
