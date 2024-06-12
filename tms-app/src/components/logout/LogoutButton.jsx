import React from "react";
import { useAuth } from "../../context/AuthProvider";
import { useNavigate } from "react-router-dom";

const LogoutButton = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      await logout();
      navigate("/");
    } catch (error) {
      console.error("failed to logout", error.message);
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
