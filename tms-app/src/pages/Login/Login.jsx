import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import LoginForm from "../../components/login/LoginForm";
import { useAuth } from "../../utils/AuthProvider";
import { navigateBasedOnRole } from "../../utils/navigation";

const Login = () => {
  const { login, isLoggedIn, user } = useAuth();
  const [loginError, setLoginError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    if (isLoggedIn) {
      if (user && user.role !== null) {
        navigateBasedOnRole(user.role, navigate);
      } else {
        console.error("No user role found");
        navigate("/");
      }
    }
  }, [isLoggedIn, user, navigate]);

  const handleLogin = async ({ email, password }) => {
    setLoginError("");
    const res = await login({ email, password });
    if (res.error) {
      setLoginError(`An Error Occurred: ${res.error}`);
    } else {
      console.log("Login successful");
      navigateBasedOnRole(res.role, navigate);
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
