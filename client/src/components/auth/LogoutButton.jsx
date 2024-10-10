import React from "react";
import { useAuth } from "../../hooks/useAuth";

const LogoutButton = () => {
  const { logout } = useAuth();

  return (
    <>
      <div className="button-container">
        <button type="button" onClick={logout}>
          Logout
        </button>
      </div>
    </>
  );
};

export default LogoutButton;
