import React, { useState } from "react";
import { useAuth } from "../../hooks/useAuth";
import Button from "react-bootstrap/Button";
import Spinner from "react-bootstrap/Spinner";
import { validators } from "../../utils/validation";

const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");

  const { login, loginStatus } = useAuth();

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
    setEmailError(validators.email(e.target.value));
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
    setPasswordError(validators.password(e.target.value));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const emailErr = validators.email(email);
    const passwordErr = validators.password(password);

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
          <Button
            variant="primary"
            type="submit"
            disabled={loginStatus === "pending"}
          >
            {loginStatus !== "pending" ? (
              "Login"
            ) : (
              <Spinner animation="border" role="loginStatus" />
            )}
          </Button>
        </div>
      </form>
    </div>
  );
};

export default LoginForm;
