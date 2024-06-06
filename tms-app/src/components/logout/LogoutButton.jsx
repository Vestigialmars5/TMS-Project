import React from "react";
import { getToken, removeToken } from "../../utils/auth";
import { useNavigate } from "react-router-dom";

const LogoutButton = () => {
  const navigate = useNavigate();
  const handleLogout = async () => {
  const token = getToken();

    try {
      const res = await fetch("http://localhost:5000/auth/logout", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({}),
      });

      if (res.ok) {
        removeToken(token);
        navigate("/");
      } else {
        console.error("Logout failed:", res.status);
      }
    } catch (error) {
      console.log("Error Logging out:", error);
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
