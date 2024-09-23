import React, { useState } from "react";
import { useAuth } from "../../hooks/useAuth";
import Spinner from "react-bootstrap/Spinner";

const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");

  const { login, loginStatus } = useAuth();

  const validateEmail = (email) => {
    if (!email) {
      return "Email is required";
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      return "Email address is invalid";
    }
    return "";
  };

  const validatePassword = (password) => {
    if (!password) {
      return "Password is required";
    } else if (password.length < 8) {
      return "Password must be at least 8 characters";
    }
    return "";
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
    setEmailError(validateEmail(e.target.value));
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
    setPasswordError(validatePassword(e.target.value));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const emailErr = validateEmail(email);
    const passwordErr = validatePassword(password);

    if (emailErr || passwordErr) {
      setEmailError(emailErr);
      setPasswordError(passwordErr);
    } else {
      login({ email, password });
    }
  };

  return (
    <div className="mainContainer">
      <form onSubmit={handleSubmit}>
        <div className="inputContainer">
          <label>Email:</label>
          <input type="email" value={email} onChange={handleEmailChange} />
          {emailError && <p>{emailError}</p>}
        </div>
        <div className="inputContainer">
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={handlePasswordChange}
          />
          {passwordError && <p>{passwordError}</p>}
        </div>
        <div className="inputContainer">
          {loginStatus !== "pending" ? (
            <button type="submit" disabled={loginStatus === "pending"}>
              Login
            </button>
          ) : (
            <Spinner animation="border" role="loginStatus" />
          )}
        </div>
      </form>
    </div>
  );
};

export default LoginForm;
