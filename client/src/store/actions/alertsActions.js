import { addAlert, removeAlert, clearAlerts } from "../slices/alertsSlice";
import { v4 as uuidv4 } from "uuid";

let store;
const duration = 5000; // 5 seconds
const alertTimeouts = new Map();

export const initializeAlertActions = (reduxStore) => {
  store = reduxStore;
};

export const showAlert = (message, type) => {
  if (!store) {
    console.error("Store Is Not Initialized");
    return;
  }

  const id = uuidv4();
  const expiresAt = Date.now() + duration; 
  store.dispatch(addAlert({ id, message, type, expiresAt }));

  const timeoutId = setTimeout(() => {
    removeAlertIfExists(id);
    alertTimeouts.delete(id);
  }, duration);

  alertTimeouts.set(id, timeoutId);
  return id;

};

export const closeAlert = (id) => {
  if (!store) {
    console.error("Store Is Not Initialized");
    return;
  }

  if (alertTimeouts.has(id)) {
    clearTimeout(alertTimeouts.get(id));
    alertTimeouts.delete(id);
  }

  store.dispatch(removeAlert(id));
};

const removeAlertIfExists = (id) => {
  if (!store) {
    console.error("Store Is Not Initialized");
    return;
  }

  const alertToRemove = store.getState().alerts.alerts.find((alert) => alert.id === id);

  if (alertToRemove) {
    store.dispatch(removeAlert(id));
  }
};

export const clearAllAlerts = () => {
  if (!store) {
    console.error("Store Is Not Initialized");
    return;
  }

  alertTimeouts.forEach((timeoutId) => clearTimeout(timeoutId));
  alertTimeouts.clear();

  store.dispatch(clearAlerts());
};
