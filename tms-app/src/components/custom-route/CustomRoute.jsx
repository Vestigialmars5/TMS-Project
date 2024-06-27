import React from "react";
import { Outlet, Navigate, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthProvider";
import { navigateBasedOnRole } from "../../utils/navigation";
import Spinner from "react-bootstrap/esm/Spinner";

const CustomRoute = ({ requiredRoleId, requiredRestriction }) => {
  const { loading, isLoggedIn, isOnboarded, isAuthorized } = useAuth();
  const navigate = useNavigate();

  console.log("Accessing a custom route");
  
  
  if (loading) {
    return <Spinner animation="border" />;
  }


  // Based on a required role
  if (requiredRoleId) {
    console.log("A role is required");
    console.log(isLoggedIn.toString());
    if (!isLoggedIn) {
      console.log("not logged in", isLoggedIn);
      return <Navigate to="/login" replace />;
    }

    if (!isAuthorized(requiredRoleId)) {
      console.log("unauthorized");
      console.log("required", requiredRoleId);
      return <Navigate to="/home" replace />;
    }
  }

  // Based on a restriction
  if (requiredRestriction) {
    console.log("restriction", requiredRestriction);
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
      case "isOnboarded":
        if (!isOnboarded) {
          return <Navigate to="/login" />;
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
