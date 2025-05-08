import React, { useEffect } from "react";
import { Navigate } from "react-router-dom";
import { Outlet } from "react-router-dom";
import { useSelector } from "react-redux";
import { useRoleBasedNavigation } from "../hooks/useRoleBasedNavigation";
import Spinner from "react-bootstrap/Spinner";
import { showAlert } from "../store/actions/alertsActions";

function PrivateRoute({ required }) {
  const { user, isAuthenticated, isAuthenticating } = useSelector(
    (state) => state.auth
  );
  const { goToDashboard } = useRoleBasedNavigation();

  useEffect(() => {
    if (!isAuthenticating && !isAuthenticated) {
      showAlert("You Must Be Logged In To Access This Page", "warning");
      return <Navigate to="/login" />;
    }

    if (!isAuthenticating && required && !required.includes(user.status)) {
      // if user didn't come from login display alert
      if (!location.pathname.startsWith("/onboarding")) {
        showAlert("You Are Not Authorized To Access This Page", "danger");
      }
      goToDashboard(user.roleId);
    }
  }, [isAuthenticating, isAuthenticated, user.roleId, goToDashboard]);

  if (isAuthenticating || !isAuthenticated) {
    return <Spinner />;
  }

  return <Outlet />;
}

export default PrivateRoute;
