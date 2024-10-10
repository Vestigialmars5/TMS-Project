// Make sure user is logged out to access pages protected by this route

import React, { useEffect } from "react";
import { Outlet, useLocation } from "react-router-dom";
import { useSelector } from "react-redux";
import { useRoleBasedNavigation } from "../hooks/useRoleBasedNavigation";
import Spinner from "react-bootstrap/Spinner";
import { showAlert } from "../store/actions/alertsActions";
import { useNavigate } from "react-router-dom";

const PublicRoute = () => {
  const { user, isAuthenticated, isAuthenticating } = useSelector(
    (state) => state.auth
  );
  const { goToDashboard } = useRoleBasedNavigation();
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    if (!isAuthenticating && isAuthenticated) {
      // if user didn't come from login display alert
      if (location.pathname !== "/login") {
        showAlert("You Are Already Logged In", "info");
      }

      if (user.status === "not_onboarded") {
        showAlert("Please Complete Your Onboarding", "warning");
        navigate("/onboarding");
      } else {
        goToDashboard(user.roleId);
      }
    }
  }, [isAuthenticating, isAuthenticated, user, goToDashboard, location.state]);

  if (isAuthenticating || isAuthenticated) {
    return <Spinner />;
  }

  return <Outlet />;
};

export default PublicRoute;
