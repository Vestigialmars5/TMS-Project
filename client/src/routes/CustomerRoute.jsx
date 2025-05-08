import { Outlet } from "react-router-dom";
import { useSelector } from "react-redux";
import { useRoleBasedNavigation } from "../hooks/useRoleBasedNavigation";
import { useEffect } from "react";
import { showAlert } from "../store/actions/alertsActions";
import Spinner from "react-bootstrap/Spinner";
import { useNavigate } from "react-router-dom";

const CustomerRoute = () => {
  const required = 4;
  const { user, isAuthenticated, isAuthenticating } = useSelector(
    (state) => state.auth
  );
  const { goToDashboard } = useRoleBasedNavigation();
  const navigate = useNavigate();

  useEffect(() => {
    if (location.pathname.startsWith("/customer")) {
      if (!isAuthenticating && !isAuthenticated) {
        showAlert("You Must Be Logged In To Access This Page", "warning");
        navigate("/login");
      }

      if (
        !isAuthenticating &&
        isAuthenticated &&
        user.status === "not_onboarded"
      ) {
        showAlert("Please Complete Your Onboarding", "warning");
        navigate("/onboarding");
      }

      if (!isAuthenticating && isAuthenticated && required !== user.roleId) {
        showAlert("You Are Not Authorized To Access This Page", "danger");
        goToDashboard(user.roleId);
      }
    }
  }, [isAuthenticating, isAuthenticated, user, goToDashboard]);

  if (isAuthenticating || !isAuthenticated) {
    return <Spinner />;
  }

  return <Outlet />;
};

export default CustomerRoute;
