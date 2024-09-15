import React from "react";
import { useAuth } from "../context/AuthProvider";
import { Navigate } from "react-router-dom";
import { Outlet } from "react-router-dom";

function PrivateRoute({ required }) {
  const { user, userStatus } = useAuth();

  if (!user) {
    return <Navigate to="/login" />;
  }

  if (required && !required.includes(userStatus)) {
    return <Navigate to="/home" />;
  }

  return <Outlet />;
}

export default PrivateRoute;
