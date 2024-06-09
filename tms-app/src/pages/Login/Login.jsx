import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import LoginForm from "../../components/login/LoginForm";
import { useAuth } from "../../utils/auth";
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
    try {
      const error = await login({ email, password });
      console.log("Gor response from login", error);
      if (error) {
        setLoginError(`An Error Occurred: ${error}`);
      } else {
        console.log("No errors Returned from response")
        if (user && user.email) {
          // Check if user is properly initialized
          console.log("Login successful");
        } else {
          console.error("User object not properly initialized");
          setLoginError("User object not properly initialized");
        }
      }
    } catch (error) {
      console.error("Login error:", error.message);
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
