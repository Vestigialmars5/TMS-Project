import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import LoginForm from "../../components/login/LoginForm";
import { authenticateUser, decodeToken } from "../../utils/auth";

const Login = () => {
  const [loginError, setLoginError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async ({ email, password }) => {
    try {
      setLoginError("");
      const res = await fetch("http://localhost:5000/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });

      const response = await res.json();

      if (!res.ok) {
        throw new Error(response.error);
      } else {
        const token = response.access_token;
        authenticateUser(token);
        console.log(decodeToken(token));
        // TODO: redirect navigate("/");
      }
    } catch (error) {
      setLoginError(`An Error Occurred: ${error.message}`);
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <LoginForm onSubmit={handleLogin} errorMessage={loginError} />
    </div>
  );
};

export default Login;
