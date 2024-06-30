import { createContext, useContext, useState, useEffect } from "react";
import { createUserApi } from "../utils/userManagement";
import { getUsersApi } from "../utils/userManagement";
import { deleteUserApi } from "../utils/userManagement";
import { updateUserApi } from "../utils/userManagement";

const UserManagementContext = createContext();

export const useUserManagement = () => useContext(UserManagementContext);

export const UserManagementProvider = ({ children }) => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [refresh, setRefresh] = useState(false);

  useEffect(() => {
    const delayTimeout = setTimeout(() => {
      setLoading(false);
    }, 500); // Modify timeout for smoothness

    return () => clearTimeout(delayTimeout);
  }, []);

  const createUser = async (userData) => {
    try {
      await createUserApi(userData);
    } catch (error) {
      console.error(error.message);
    }
  };

  const getUsers = async (args) => {
    try {
      const data = await getUsersApi(args);
      setUsers(data);
      return data;
    } catch (error) {
      console.error(error.message);
      return {};
    }
  };

  const deleteUser = async (userId) => {
    try {
      await deleteUserApi(userId);
    } catch (error) {
      console.error(error.message);
    }
  };

  const updateUser = async (userData) => {
    try {
      await updateUserApi(userData);
    } catch (error) {
      console.error(error.message);
    }
  };

  const refreshUsers = () => {
    setRefresh(!refresh);
  };

  return (
    <UserManagementContext.Provider
      value={{ createUser, getUsers, deleteUser, updateUser, refreshUsers, users, loading, refresh }}
    >
      {children}
    </UserManagementContext.Provider>
  );
};
