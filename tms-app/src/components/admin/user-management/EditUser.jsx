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
  const [emailError, setEmailError] = useState("");
  const [usernameError, setUsernameError] = useState("");
  const [roleError, setRoleError] = useState("");
  const [userId, setUserId] = useState(user.id);

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

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
    setEmailError(validateEmail(e.target.value));
  };

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handleRoleChange = (e) => {
    setRole(e.target.value);
  };

  const handleUpdateUser = async (e) => {
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
        console.log("trying updating");
        await updateUser(userId, username, email, role);
        await refreshUsers();
      } catch (error) {
        console.error(error.message);
      }
    }
  };

  return (
    <div>
      <h1>Edit User</h1>
      <Form>
        <Form.Group controlId="username">
          <Form.Label>Username</Form.Label>
          <Form.Control
            type="text"
            defaultValue={user.username}
            onChange={handleUsernameChange}
          />
        </Form.Group>

        <Form.Group controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            type="email"
            defaultValue={user.email}
            onChange={handleEmailChange}
          />
        </Form.Group>

        <Form.Group controlId="role">
          <Form.Label>Role</Form.Label>
          <Form.Control
            as="select"
            defaultValue={user.role}
            onChange={handleRoleChange}
          >
            {ROLES.map((role, index) => (
              <option key={index}>{role}</option>
            ))}
          </Form.Control>
        </Form.Group>

        <Button variant="primary" type="submit" onSubmit={handleUpdateUser}>
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
