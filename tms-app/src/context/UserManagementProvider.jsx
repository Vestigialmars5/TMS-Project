import { createContext, useContext, useState, useEffect } from "react";
import { createUser as createUserApi } from "../utils/userManagement";
import { getUsers as getUsersApi } from "../utils/userManagement";

const UserManagementContext = createContext();

export const useUserManagement = () => useContext(UserManagementContext);

export const UserManagementProvider = ({ children }) => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const delayTimeout = setTimeout(() => {
      setLoading(false);
    }, 500); // Modify timeout for smoothness

    return () => clearTimeout(delayTimeout);
  }, []);

  useEffect(() => {
    const delayTimeout = setTimeout(() => {
      setLoading(false);
    }, 0); // Modify timeout for smoothness

    return () => clearTimeout(delayTimeout);
  }, []);

  const createUser = async (userData) => {
    try {
      await createUserApi(userData);
    } catch (error) {
      console.error("Creation failed", error.message);
    }
  };

  const getUsers = async (args) => {
    try {
      const data = await getUsersApi(args);
      setUsers(data);
      return data;
    } catch (error) {
      console.error("Error with the api", error.message);
      return {};
    }
  };

  return (
    <UserManagementContext.Provider value={{ createUser, getUsers, users, loading }}>
      {children}
    </UserManagementContext.Provider>
  );
};
