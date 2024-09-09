import { createContext, useContext, useState, useEffect } from "react";
import {
  createUserApi,
  getUsersApi,
  deleteUserApi,
  updateUserApi,
  getRolesApi,
} from "../utils/userManagement";

const UserManagementContext = createContext();

export const useUserManagement = () => useContext(UserManagementContext);

export const UserManagementProvider = ({ children }) => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [refresh, setRefresh] = useState(false);
  const [roles, setRoles] = useState([]);

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
      throw new Error(error.message);
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
      throw new Error(error.message);
    }
  };

  const updateUser = async (userData) => {
    try {
      const response = await updateUserApi(userData);
      if (response) {
        throw new Error(response);
      }
    } catch (error) {
      throw new Error(error.message);
    }
  };

  const refreshUsers = () => {
    setRefresh(!refresh);
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

  return (
    <UserManagementContext.Provider
      value={{
        createUser,
        getUsers,
        deleteUser,
        updateUser,
        refreshUsers,
        getRoles,
        roles,
        users,
        loading,
        refresh,
      }}
    >
      {children}
    </UserManagementContext.Provider>
  );
};
