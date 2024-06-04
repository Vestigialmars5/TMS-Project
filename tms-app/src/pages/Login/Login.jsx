import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import LoginForm from "../../components/Login/LoginForm";

/* 
const Login1 = (props) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");

  const navigate = useNavigate();

  const validateInputs = () => {
    // Set initial error values to empty
    setEmailError("");
    setPasswordError("");

    // Check if the user has entered both fields correctly
    if (email === "") {
      setEmailError("Please enter your email");
      return false;
    }

    if (!/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email)) {
      setEmailError("Please enter a valid email");
      return false;
    }

    if (password === "") {
      setPasswordError("Please enter a password");
      return false;
    }

    if (password.length < 8) {
      setPasswordError("The password must be 8 characters or longer");
      return false;
    }

    return true;

    // Authentication calls will be made here...
  };

  const handleLogin = () => {
    if (validateInputs()) {
      // TODO: Authenticate login
      // TODO: Redirect to appropriate dashboard
      navigate("/NoPage");
    }
  };

  return (
    <LoginForm
      email={email}
      setEmail={setEmail}
      password={password}
      setPassword={setPassword}
      emailError={emailError}
      passwordError={passwordError}
      handleLogin={handleLogin}
    />
  );
}; */

const Login = () => {
  const [loginError, setLoginError] = useState("");

  const checkLoginCredentials = async (email, password) => {
    try {
      const res = await fetch("http://localhost:5000/auth/CheckLoginCredentials", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({email, password}),
      });

      if (res.ok) {
        return await res.json();
      } else if (res.status == 400) {
        const errorResponse = await res.json();
        throw new Error(errorResponse.error);
      } else {
        throw new Error("Error Getting Data From API");
      }
    } catch (error) {
      throw new Error(error.message);
    }
  };

  const handleLogin = async ({ email, password }) => {
    try {
      setLoginError("");
      const response = await checkLoginCredentials(email, password);
      if (response.success) {
        console.log("SUCCESS");
      } else {
        setLoginError("Invalid Credentials");
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
