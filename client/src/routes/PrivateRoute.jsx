import React from "react";
import { Navigate } from "react-router-dom";
import { Outlet } from "react-router-dom";
import { useSelector } from "react-redux";

function PrivateRoute({ required }) {
  const auth = useSelector((state) => state.auth);

  if (!auth.isAuthenticated) {
    console.log("Not Authenticated, Redirecting To Login");
    return <Navigate to="/login" />;
  }

  if (required && !required.includes(auth.user.status)) {
    return <Navigate to="/home" />;
  }

  return <Outlet />;
}

export default PrivateRoute;
