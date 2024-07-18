import React from "react";
import { useAuth } from "../../context/AuthProvider";
import { useNavigate } from "react-router-dom";
import { useAlert } from "../../context/AlertProvider";

const LogoutButton = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();
  const { addAlert } = useAlert();

  const handleLogout = async () => {
    try {
      await logout();
      addAlert("Logout successful", "success");
      navigate("/");
    } catch (error) {
      addAlert(error.message, "danger");
    }
  };

  return (
    <>
      <div className="button-container">
        <button type="button" onClick={handleLogout}>
          Logout
        </button>
      </div>
    </>
  );
};

export default LogoutButton;
