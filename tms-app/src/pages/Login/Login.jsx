import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import LoginForm from "../../components/login/LoginForm";
import { useAuth } from "../../context/AuthProvider";
import { navigateBasedOnRole } from "../../utils/navigation";

const Login = () => {
  const { login, isOnboarded, user } = useAuth();
  const [loginError, setLoginError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async ({ email, password }) => {
    setLoginError("");
    const res = await login({ email, password });
    if (res?.error) {
      setLoginError(res.error);
    } else {
      // TODO: Display success
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
