import React from "react";
import { Outlet, Navigate, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthProvider";
import { navigateBasedOnRole } from "../../utils/navigation";
import Spinner from "react-bootstrap/esm/Spinner";

const CustomRoute = ({ requiredRoleId, requiredRestrictions = [] }) => {
  const { user, loading, isLoggedIn, isOnboarded, isAuthorized } = useAuth();
  const navigate = useNavigate();

  if (loading) {
    return <Spinner animation="border" />;
  }

  // Based on a required role
  if (requiredRoleId) {
    console.log(isLoggedIn.toString());
    if (!isLoggedIn) {
      return <Navigate to="/login" replace />;
    }

    if (!isAuthorized(requiredRoleId)) {
      return <Navigate to="/home" replace />;
    }
  }

  // Based on a restriction
  for (let restriction of requiredRestrictions) {
    switch (restriction) {
      case "loggedIn":
        if (!isLoggedIn) {
          return <Navigate to="/login" />;
        }
        break;
      case "loggedOut":
        if (isLoggedIn) {
          return <Navigate to="/" />;
        }
        break;
      case "notOnboarded":
        if (isOnboarded) {
          return <Navigate to="/home" />;
        }
        break;
      default:
        return navigateBasedOnRole(user?.role, navigate);
    }
  }

  return <Outlet />;
};

export default CustomRoute;
