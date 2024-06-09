import React from "react";
import { Outlet, Navigate } from "react-router-dom";
import { useAuth } from "../../utils/auth";

const PrivateRoute = ({ requiredRole }) => {
  const { isLoggedIn, isAuthorized } = useAuth();

  if (!isLoggedIn) {
    console.log("not logged in");
    return <Navigate to="/login" replace />;
  }

  if (!isAuthorized(requiredRole)) {
    console.log("unauthorized");
    console.log("required", requiredRole);
    return <Navigate to="/home" replace />;
  }

  return <Outlet />;
};

export default PrivateRoute;
