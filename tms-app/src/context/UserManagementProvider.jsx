import { createContext, useContext } from "react";
import { createUser as createUserApi } from "../utils/userManagement";

const UserManagementContext = createContext();

export const useUserManagement = () => useContext(UserManagementContext);

export const UserManagementProvider = ({ children }) => {
  const createUser = async (userData) => {
    try {
        await createUserApi(userData);
    } catch (error) {
        console.error("Creation failed", error.message);
    }
  };

  return (
    <UserManagementContext.Provider
      value={{ createUser }}
    >
      {children}
    </UserManagementContext.Provider>
  );
};
