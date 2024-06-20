import React from "react";
import { Outlet, Navigate, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthProvider";
import { navigateBasedOnRole } from "../../utils/navigation";
import Spinner from "react-bootstrap/esm/Spinner";

const CustomRoute = ({ requiredRole, requiredRestriction }) => {
  const { loading, isLoggedIn, isAuthorized } = useAuth();
  const navigate = useNavigate();

  console.log("Accessing a custom route", isLoggedIn.toString());
  
  
  if (loading) {
    return <Spinner animation="border" />;
  }


  // Based on a required role
  if (requiredRole) {
    console.log("A role is required");
    console.log(isLoggedIn.toString());
    if (!isLoggedIn) {
      console.log("not logged in", isLoggedIn);
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
    console.log("restriction");
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
