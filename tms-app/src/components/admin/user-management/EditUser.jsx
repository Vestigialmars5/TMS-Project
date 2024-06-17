import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { useUserManagement } from "../../../context/UserManagementProvider";
import { useState } from "react";

const ROLES = [
  "admin",
  "transportation manager",
  "carrier",
  "customer/shipper",
  "driver",
  "accounting",
  "warehouse manager",
];

const EditUser = ({ user, cancelEdit }) => {
  const { updateUser, refreshUsers } = useUserManagement();
  const [username, setUsername] = useState(user.username);
  const [email, setEmail] = useState(user.email);
  const [role, setRole] = useState(user.role);
  const [userId, setUserId] = useState(user.id);
  const [emailError, setEmailError] = useState("");
  const [usernameError, setUsernameError] = useState("");
  const [roleError, setRoleError] = useState("");

  const validateUsername = (username) => {
    if (!username) {
      return "Username is required";
    }
    // TODO: More validations
    return "";
  };

  const validateEmail = (email) => {
    if (!email) {
      return "Email is required";
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      return "Email addres is invalid";
    }
    return "";
  };

  const validateRole = (role) => {
    if (!ROLES.includes(role)) {
      return "Invalid role";
    }
    return "";
  };

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
    setUsernameError(validateUsername(e.target.value));
    console.log("username", e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
    setEmailError(validateEmail(e.target.value));
  };

  const handleRoleChange = (e) => {
    setRole(e.target.value);
    setRoleError(validateRole(e.target.value));
  };

  const handleEditUser = async (e) => {
    e.preventDefault();
    const emailErr = validateEmail(email);
    const usernameErr = validateUsername(username);
    const roleErr = validateRole(role);

    // TODO: Validations
    if (emailError || usernameError || roleError) {
      setEmailError(emailErr);
      setUsernameError(usernameErr);
      setRoleError(roleErr);
    } else {
      try {
        await updateUser({userId, username, email, role});
        await refreshUsers();
        cancelEdit();
      } catch (error) {
        console.error(error.message);
      }
    }
  };

  return (
    <div>
      <h1>Edit User</h1>
      <Form onSubmit={handleEditUser}>
        <Form.Group controlId="username">
          <Form.Label>Username</Form.Label>
          <Form.Control
            type="text"
            defaultValue={username}
            onChange={handleUsernameChange}
          />
          {usernameError && <p>{usernameError}</p>}
        </Form.Group>

        <Form.Group controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            type="email"
            defaultValue={email}
            onChange={handleEmailChange}
          />
          {emailError && <p>{emailError}</p>}
        </Form.Group>

        <Form.Group controlId="role">
          <Form.Label>Role</Form.Label>
          <Form.Control
            as="select"
            defaultValue={role}
            onChange={handleRoleChange}
          >
            {ROLES.map((role, index) => (
              <option key={index}>{role}</option>
            ))}
          </Form.Control>
          {roleError && <p>{roleError}</p>}
        </Form.Group>

        <Button variant="primary" type="submit">
          Save
        </Button>
        <Button variant="secondary" type="button" onClick={cancelEdit}>
          Cancel
        </Button>
      </Form>
    </div>
  );
};

export default EditUser;
