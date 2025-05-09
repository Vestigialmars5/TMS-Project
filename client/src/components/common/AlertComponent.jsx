import React from "react";
import { closeAlert } from "../../store/actions/alertsActions";
import Alert from "react-bootstrap/Alert";

const AlertComponent = ({ id, message, type }) => {

  return (
    <Alert variant={type} onClose={() => closeAlert(id)} dismissible>
      {message}
    </Alert>
  );
};

export default AlertComponent;
