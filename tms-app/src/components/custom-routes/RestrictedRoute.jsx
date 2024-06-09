import React from "react";
import { Navigate, Outlet, useNavigate } from "react-router-dom";
import { useAuth } from "../../utils/auth";
import { navigateBasedOnRole } from "../../utils/navigation";

const RestrictedRoute = ({ requiredRestriction }) => {
  const { isLoggedIn, user } = useAuth();
  const navigate = useNavigate();

  switch (requiredRestriction) {
    case "loggedIn":
        if (!isLoggedIn) {
            return <Navigate to="/login" />
        }
        break;
    case "loggedOut":
        if (isLoggedIn) {
            return <Navigate to="/" />
        }
        break;
    default:
        console.log("Restricted");
        return navigateBasedOnRole(user?.role, navigate);
  }

  return <Outlet />;
};

export default RestrictedRoute;
