import React from "react";

const LoginForm = ({
  email,
  setEmail,
  password,
  setPassword,
  emailError,
  passwordError,
  handleLogin,
}) => {
  return (
    <div className="mainContainer">
      <div className="titleContainer">Login</div>
      <div className="inputContainer">
        <input
          value={email}
          placeholder="Enter your email here"
          onChange={(e) => setEmail(e.target.value)}
          className="inputBox"
        />
        <label className="errorLabel">{emailError}</label>
      </div>
      <div className="inputContainer">
        <input
          value={password}
          placeholder="Enter your password here"
          onChange={(e) => setPassword(e.target.value)}
          className="inputBox"
        />
        <label className="errorLabel">{passwordError}</label>
      </div>
      <div className="inputContainer">
        <input
          className="inputButton"
          type="button"
          onClick={handleLogin}
          value="Log in"
        />
      </div>
    </div>
  );
};

export default LoginForm;
