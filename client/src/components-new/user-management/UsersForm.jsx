import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Spinner from "react-bootstrap/Spinner";
import { useQuery, QueryClient } from "@tanstack/react-query";
import { getRoles } from "../../services/usersService";
import { useUsers } from "../../hooks/useUsers";
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
    isLoading: rolesLoading,
    error: rolesError,
  } = useQuery({ queryKey: ["roles"], queryFn: getRoles });
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
      console.log("Create User");
      createUser({ email, password, roleId });
    }
  };

  if (rolesLoading) {
    return (
      <Button variant="primary" disabled>
        <Spinner animation="border" role="status" />
        Loading Roles...
      </Button>
    );
  }

  if (rolesError) {
    console.error(rolesError);
    return <p>Error loading roles</p>;
  }

  return (
    <div>
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
          <Form.Control as="select" value={roleId} onChange={handleRoleChange}>
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
              <Spinner animation="border" role="createUserStatus" />
            )}
          </Button>
        </Form.Group>
      </Form>
    </div>
  );
};

export default UsersForm;
