import { createContext, useContext, useEffect, useState } from "react";
import { loginApi, logoutApi } from "../utils/auth";
import { getRolesApi } from "../utils/common";
import { decodeToken, getToken } from "../utils/tokenFunctions";
import { useNavigate } from "react-router-dom";
import { navigateBasedOnRole } from "../utils/navigation";

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [user, setUser] = useState(null);
  const [userStatus, setUserStatus] = useState(null);
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
      setUserStatus(decoded.status);
    
      // Using this casing to avoid renaming from the db
      if (decoded.status == "not_onboarded") {
        navigate("/onboarding");
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
      const userData = await loginApi(credentials);

      const roleName = userData.roleName;
      const userStatus = userData.status;
      setUser(userData);
      setIsLoggedIn(true);
      setUserStatus(userStatus);
      if (userStatus === "not_onboarded") {
        navigate("/onboarding");
      } else {
        navigateBasedOnRole(roleName, navigate);
      }
    } catch (error) {
      return { error: error.message };
    }
  };

  const logout = async () => {
    try {
      await logoutApi();
      setUser(null);
      setIsLoggedIn(false);
    } catch (error) {
      throw new Error(error.message);
    }
  };

  // Including getRoles in auth context to not cluster the app with too many contexts 
  // If there are more functions added to common, then a common context will be necessary
  // For now just manage it from here
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
        user,
        userStatus,
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
