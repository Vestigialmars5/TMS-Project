import React, { useState } from "react";

const ROLES = [
  "admin",
  "transportation manager",
  "carrier",
  "customer/shipper",
  "driver",
  "accounting",
  "warehouse manager",
];

const CreateUserForm = ({ onSubmit, errorMessage }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("");
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [roleError, setRoleError] = useState("");
  const [selected, setSelected] = useState("Select Role");

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

  // TODO: Validate role
  const validateRole = (role) => {
    if (!ROLES.includes(role)) {
      return "Invalid role";
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

  const handleRoleChange = (e) => {
    setRole(e.target.value);
    setRoleError(validateRole(e.target.value));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const emailErr = validateEmail(email);
    const passwordErr = validatePassword(password);
    const roleErr = validateRole(role);

    if (emailErr || passwordErr || roleErr) {
      setEmailError(emailErr);
      setPasswordError(passwordErr);
      setRoleError(roleErr);
    } else {
      onSubmit({ email, password, role });
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
          <label htmlFor="role">Role:</label>
          <select
            name="role"
            id="role"
            defaultValue={selected}
            onChange={handleRoleChange}
          >
            <option disabled value={"Select Role"}>
              Select Role
            </option>
            {ROLES.map((role, index) => (
              <option key={index} value={role}>
                {role.charAt(0).toUpperCase() + role.slice(1)}
              </option>
            ))}
          </select>
          {roleError && <p>{roleError}</p>}
        </div>
        <div className="inputContainer">
          {errorMessage && <p>{errorMessage}</p>}
          <button type="submit">Create User</button>
        </div>
      </form>
    </div>
  );
};

export default CreateUserForm;
