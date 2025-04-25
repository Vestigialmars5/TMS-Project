import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Spinner from "react-bootstrap/Spinner";
import { useUsers } from "../../hooks/useUsers";
import { useRoles } from "../../hooks/useRoles";
import Button from "react-bootstrap/Button";

const UsersForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [roleId, setRoleId] = useState(0);
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [roleError, setRoleError] = useState("");

  const {
    data: roles,
    status: rolesStatus,
    error: rolesError,
  } = useRoles();
  const { createUser, createUserStatus } = useUsers();

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

  const validateRole = (roleId) => {
    if (!roles.some((role) => role.roleId === roleId)) {
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
      console.log("Error");
    } else {
      createUser({ email, password, roleId });
    }
  };

  if (rolesError) {
    const message =
      rolesError.response?.data?.description ||
      rolesError.response?.data?.error ||
      "An Unknown Error Occurred";
    console.error(rolesError);
    showAlert(`Error Retrieving Roles: ${message}`, "danger");
  }

  return (
    <div>
      {rolesStatus !== "pending" ? (
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId="email">
            <Form.Label>Email</Form.Label>
            <Form.Control
              type="email"
              value={email}
              onChange={handleEmailChange}
            />
            {emailError && <p>{emailError}</p>}
          </Form.Group>
          <Form.Group controlId="password">
            <Form.Label>Password</Form.Label>
            <Form.Control
              type="password"
              value={password}
              onChange={handlePasswordChange}
            />
            {passwordError && <p>{passwordError}</p>}
          </Form.Group>
          <Form.Group controlId="role">
            <Form.Label>Role</Form.Label>
            <Form.Control
              as="select"
              value={roleId}
              onChange={handleRoleChange}
            >
              <option value={0}>Select a Role</option>
              {roles.map((role) => (
                <option key={role.roleId} value={role.roleId}>
                  {role.roleName}
                </option>
              ))}
            </Form.Control>
            {roleError && <p>{roleError}</p>}
          </Form.Group>
          <Form.Group>
            <Button
              variant="primary"
              type="submit"
              disabled={createUserStatus === "pending"}
            >
              {createUserStatus !== "pending" ? (
                "Create User"
              ) : (
                <Spinner animation="border" role="status" />
              )}
            </Button>
          </Form.Group>
        </Form>
      ) : rolesError ? (
        <p>There was an error getting roles</p>
      ) : (
        <Spinner animation="border" role="status" />
      )}
    </div>
  );
};

export default UsersForm;
