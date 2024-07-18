import React from "react";
import { useNavigate } from "react-router-dom";

const LoginButton = () => {
  const navigate = useNavigate();

  const handleClick = () => {
    return navigate("/login");
  };

  return (
    <>
      <button type="button" onClick={handleClick}>
        Login
      </button>
    </>
  );
};

export default LoginButton;
