import React from "react";
import { useAuth } from "../../utils/auth";
import { useNavigate } from "react-router-dom";

const LogoutButton = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    const error = await logout();
    if (error) {
      console.log(error);
    } else {
      navigate("/");
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
