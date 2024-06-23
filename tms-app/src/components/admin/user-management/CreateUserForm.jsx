import React, { useEffect, useState } from "react";
import { useAuth } from "../../../context/AuthProvider";

const CreateUserForm = ({ onSubmit, errorMessage }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [roleId, setRoleId] = useState(0);
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [roleError, setRoleError] = useState("");
  const [selected, setSelected] = useState("Select Role");
  const { getRoles, roles } = useAuth();

  useEffect(() => {
    if (roles.length === 0) {
      getRoles();
    }
  }, []);

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
  const validateRole = (roleId) => {
    if (!roles.some(role => role.roleId === roleId)) {
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
    const idString = e.target.value;
    const idInt = parseInt(idString);
    setRoleId(idInt);
    setRoleError(validateRole(idInt));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const emailErr = validateEmail(email);
    const passwordErr = validatePassword(password);
    const roleErr = validateRole(roleId);

    if (emailErr || passwordErr || roleErr) {
      setEmailError(emailErr);
      setPasswordError(passwordErr);
      setRoleError(roleErr);
    } else {
      onSubmit({ email, password, roleId });
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
            {roles.map((role, index) => (
              <option key={index} value={role.roleId}>
                {role.roleName.charAt(0).toUpperCase() + role.roleName.slice(1)}
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
