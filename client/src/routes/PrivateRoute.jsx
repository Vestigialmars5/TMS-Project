import React from "react";
import { Navigate } from "react-router-dom";
import { Outlet } from "react-router-dom";
import { useSelector } from "react-redux";

function PrivateRoute({ required }) {
  const authState = useSelector((state) => state.auth);

  if (!authState.isAuthenticated) {
    console.log("Not Authenticated, Redirecting To Login");
    return <Navigate to="/login" />;
  }

  if (required && !required.includes(authState.user.status)) {
    return <Navigate to="/home" />;
  }

  return <Outlet />;
}

export default PrivateRoute;
