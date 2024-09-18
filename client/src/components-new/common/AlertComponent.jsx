import React, {useEffect } from "react";
import { useAlerts } from "../../hooks/useAlerts";
import Alert from "react-bootstrap/Alert";


const AlertComponent = ({ id, message, type }) => {
  const { closeAlert } = useAlerts();

  return (
    <Alert variant={type} onClose={() => closeAlert(id)} dismissible>
      {message}
    </Alert>
  );
};

export default AlertComponent;