/* import React from "react";
import Alert from "react-bootstrap/Alert";
import { useAlertOld } from "../../context/AlertProvider";

const AlertComponent = () => {
  const { alert, removeAlert } = useAlertOld();

  if (!alert) {
    return null;
  }

  return (
    <Alert variant={alert.variant} onClose={removeAlert} dismissible>
      {alert.message}
    </Alert>
  );
};

export default AlertComponent;
 */