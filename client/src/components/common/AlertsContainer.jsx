import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import AlertComponent from "./AlertComponent";
import styles from "./AlertsContainer.module.css";
import { removeAlert } from "../../store/slices/alertsSlice";

const AlertsContainer = () => {
  const alertsState = useSelector((state) => state.alerts);
  const dispatch = useDispatch();

  useEffect(() => {
    const now = Date.now();
    const expiredAlerts = alertsState.alerts.filter(
      (alert) => alert.expiresAt && alert.expiresAt < now
    );

    expiredAlerts.forEach((alert) => {
      dispatch(removeAlert(alert.id));
    });

    const intervalId = setInterval(() => {
      const currentTime = Date.now();
      const expired = alertsState.alerts.filter(
        (alert) => alert.expiresAt && alert.expiresAt < currentTime
      );
      expired.forEach((alert) => {
        dispatch(removeAlert(alert.id));
      });
    }, 1000);

    return () => clearInterval(intervalId);
  }, [alertsState.alerts, dispatch]);

  return (
    <div className={styles.container}>
      {alertsState.alerts.map((alert) => (
        <AlertComponent key={alert.id} {...alert} />
      ))}
    </div>
  );
};

export default AlertsContainer;
