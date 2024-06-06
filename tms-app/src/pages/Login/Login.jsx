import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import LoginForm from "../../components/login/LoginForm";
import {
  isAuthenticated,
  authenticateUser,
  decodeToken,
  getToken,
  getUserRole,
} from "../../utils/auth";
import { navigateBasedOnRole } from "../../utils/navigation";

const Login = () => {
  const [loginError, setLoginError] = useState("");
  const navigate = useNavigate();

  if (isAuthenticated()) {
    const token = getToken();
    const userRole = getUserRole(token);
    if (userRole !== null) {
      navigateBasedOnRole(userRole);
    } else {
      console.error("No user role found");
      return navigate("/");
    }
  }

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
        navigate("/admin/admin-dashboard");
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
