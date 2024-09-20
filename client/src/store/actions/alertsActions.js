import { addAlert, removeAlert, clearAlerts } from "../slices/alertsSlice";
import { v4 as uuidv4 } from "uuid";

let store;

export const initializeAlertActions = (reduxStore) => {
  store = reduxStore;
};

export const showAlert = (message, type) => {
  if (!store) {
    console.error("Store Is Not Initialized");
    return;
  }

  const id = uuidv4();
  store.dispatch(addAlert({ id, message, type }));

  setTimeout(() => {
    // Alert may not exist if it was closed before timeout
    const alertToRemove = store
      .getState()
      .alerts.alerts.find((alert) => alert.id === id);
    if (alertToRemove) {
      store.dispatch(removeAlert(id));
    }
  }, 5000);
};

export const closeAlert = (id) => {
  if (!store) {
    console.error("Store Is Not Initialized");
    return;
  }

  store.dispatch(removeAlert(id));
};

export const clearAllAlerts = () => {
  if (!store) {
    console.error("Store Is Not Initialized");
    return;
  }

  store.dispatch(clearAlerts());
};
