import React, { useState } from "react";

const LoginForm = ({ onSubmit, errorMessage }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");

  const validateEmail = (email) => {
    if (!email) {
      return "Email is required";
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      return "Email addres is invalid";
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
      onSubmit({ email, password });
    }
  };

  return (
    <div className="mainContainer">
      <div className="titleContainer">Login</div>
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
          {errorMessage && <p>{errorMessage}</p>}
          <button type="submit">Login</button>
        </div>
      </form>
    </div>
  );
};

export default LoginForm;
