import React from "react";
import { Outlet, Navigate, useNavigate } from "react-router-dom";
import { useAuth } from "../../utils/auth";
import { navigateBasedOnRole } from "../../utils/navigation";

const CustomRoute = ({ requiredRole, requiredRestriction }) => {
  const { isLoggedIn, isAuthorized } = useAuth();
  const navigate = useNavigate();

  // Based on a required role
  if (requiredRole) {
    if (!isLoggedIn) {
      console.log("not logged in");
      return <Navigate to="/login" replace />;
    }

    if (!isAuthorized(requiredRole)) {
      console.log("unauthorized");
      console.log("required", requiredRole);
      return <Navigate to="/home" replace />;
    }
  }

  // Based on a restriction
  if (requiredRestriction) {
    switch (requiredRestriction) {
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
      default:
        console.log("Restricted");
        return navigateBasedOnRole(user?.role, navigate);
    }
  }

  return <Outlet />;
};

export default CustomRoute;
