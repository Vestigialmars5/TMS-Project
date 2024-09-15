// Make sure user is logged out to access pages protected by this route

import React from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthProvider";
import { Outlet } from "react-router-dom";

const PublicRoute = () => {
  const { user } = useAuth();

  if (user) {
    return <Navigate to="/home" />;
  }

  return <Outlet />;
};

export default PublicRoute;
