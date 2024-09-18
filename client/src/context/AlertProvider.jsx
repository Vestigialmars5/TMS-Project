import { createContext } from "react";
import { useContext, useState } from "react";

const AlertProviderContext = createContext();

export const useAlert = () => useContext(AlertProviderContext);

export const AlertProvider = ({ children }) => {
  const [alert, setAlert] = useState(null);

  const addAlertOld = (message, variant) => {
    setAlert({ message, variant });
  };

  const removeAlert = () => {
    setAlert(null);
  };

  return (
    <AlertProviderContext.Provider value={{ alert, addAlertOld, removeAlert }}>
      {children}
    </AlertProviderContext.Provider>
  );
};
