import React, { useEffect, useState } from "react";
import LoginForm from "../../components-new/auth/LoginForm";
import { useAuth } from "../../context/AuthProvider";
import { useAlert } from "../../context/AlertProvider";

const Login = () => {
  const { login } = useAuth();
  const [loginError, setLoginError] = useState("");
  const { addAlert } = useAlert();

  const handleLogin = async ({ email, password }) => {
    setLoginError("");
    const res = await login({ email, password });
    if (res?.error) {
      setLoginError(res.error);
    } else {
      // TODO: Display success
      console.log("login");
      addAlert("Login Successful", "success");
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
