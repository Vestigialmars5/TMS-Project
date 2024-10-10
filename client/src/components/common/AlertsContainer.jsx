import React from "react";
import { useSelector } from "react-redux";
import AlertComponent from "./AlertComponent";


const AlertsContainer = () => {
  const alertsState = useSelector((state) => state.alerts);

  return (
    <div>
      {alertsState.alerts.map((alert) => (
        <AlertComponent key={alert.id} {...alert} />
      ))}
    </div>
  );
};

export default AlertsContainer;
