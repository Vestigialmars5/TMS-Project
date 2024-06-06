import React from "react";
import { Outlet, Navigate } from "react-router-dom";
import { isAuthenticated, isAuthorized } from "../../utils/auth";

const PrivateRoute = ({ requiredRole }) => {
  const authenticated = isAuthenticated();
  const authorized = isAuthorized(requiredRole);

  if (!authenticated) {
    console.log("unauthenticated");
    return <Navigate to="/login" replace />
  }

  

  if (!authorized) {
    console.log("unauthorized");
    console.log("required", requiredRole);
    return <Navigate to="/home" replace />
  }

  return <Outlet />
};

export default PrivateRoute;