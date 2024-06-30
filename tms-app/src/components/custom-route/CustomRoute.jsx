import React from "react";
import { Outlet, Navigate, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthProvider";
import { navigateBasedOnRole } from "../../utils/navigation";
import Spinner from "react-bootstrap/esm/Spinner";
import { useAlert } from "../../context/AlertProvider";

const CustomRoute = ({ requiredRoleId, requiredRestrictions = [] }) => {
  const { user, loading, isLoggedIn, isOnboarded, isAuthorized } = useAuth();
  const { addAlert } = useAlert();
  const navigate = useNavigate();

  if (loading) {
    return <Spinner animation="border" />;
  }

  // Based on a required role
  if (requiredRoleId) {
    if (!isLoggedIn) {
      addAlert("You Need To Be Logged In To Access This Page", "warning");
      return <Navigate to="/login" replace />;
    }

    if (!isAuthorized(requiredRoleId)) {
      addAlert("You Are Not Authorized To Access This Page", "warning");
      return <Navigate to="/home" replace />;
    }
  }

  // Based on a restriction
  for (let restriction of requiredRestrictions) {
    switch (restriction) {
      case "loggedIn":
        if (!isLoggedIn) {
          addAlert("You Need To Be Logged In To Access This Page", "warning");
          return <Navigate to="/login" />;
        }
        break;
      case "loggedOut":
        if (isLoggedIn) {
          addAlert("You Are Already Logged In", "warning");
          return <Navigate to="/" />;
        }
        break;
      case "notOnboarded":
        if (isOnboarded) {
          addAlert("You Have Already Onboarded", "warning");
          return <Navigate to="/home" />;
        }
        break;
      default:
        addAlert("Something Went Wrong (Restriction)", "warning");
        return navigateBasedOnRole(user?.role, navigate);
    }
  }

  return <Outlet />;
};

export default CustomRoute;
