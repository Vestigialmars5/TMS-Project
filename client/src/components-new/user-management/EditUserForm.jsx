import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { useRoles } from "../../hooks/useRoles";
import { useUsers } from "../../hooks/useUsers";
import { showAlert } from "../../store/actions/alertsActions";
import Spinner from "react-bootstrap/Spinner";

const EditUserForm = ({ user, cancelEdit }) => {
  const {
    data: roles,
    isLoading: rolesLoading,
    error: rolesError,
  } = useRoles();
  const { updateUser, updateUserStatus } = useUsers();

  const [email, setEmail] = useState(user.email);
  const [roleId, setRoleId] = useState(user.roleId);
  const [roleName, setRoleName] = useState(user.roleName);
  const [userId, setUserId] = useState(user.userId);
  const [emailError, setEmailError] = useState("");
  const [roleError, setRoleError] = useState("");

  const handleCancelEdit = () => {
    showAlert("Edit Cancelled", "info");
    cancelEdit();
  };

  const getRoleName = (roleId) => {
    const role = roles.find((role) => role.roleId === roleId);
    return role ? role.roleName : "Invalid role";
  };

  const validateEmail = (email) => {
    if (!email) {
      return "Email is required";
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      return "Email address is invalid";
    }
    return "";
  };

  const validateRole = (roleId) => {
    console.log("roles", roleId);
    if (!roles.some((role) => role.roleId === roleId)) {
      return "Invalid role";
    }
    setRoleName(getRoleName(roleId));
    return "";
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
    setEmailError(validateEmail(e.target.value));
  };

  const handleRoleChange = (e) => {
    const idString = e.target.value;
    const idInt = parseInt(idString);
    setRoleId(idInt);
    setRoleError(validateRole(idInt));
  };

  const handleEditUser = async (e) => {
    e.preventDefault();
    const emailErr = validateEmail(email);
    const roleErr = validateRole(roleId);

    // TODO: Validations
    if (emailError || roleError) {
      setEmailError(emailErr);
      setRoleError(roleErr);
    } else {
      updateUser({ userId, email, roleId });
    }
  };

  if (updateUserStatus === "success") {
    cancelEdit();
  }

  return (
    <>
      <Form onSubmit={handleEditUser}>
        <Form.Group controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            type="email"
            defaultValue={email}
            onChange={handleEmailChange}
            autoFocus
          />
          {emailError && <p>{emailError}</p>}
        </Form.Group>

        <Form.Group controlId="role">
          <Form.Label>Role</Form.Label>
          <Form.Control as="select" value={roleId} onChange={handleRoleChange}>
            <option value={0}>{roleName}</option>
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
            disabled={updateUserStatus === "pending"}
          >
            {updateUserStatus !== "pending" ? (
              "Update"
            ) : (
              <Spinner animation="border" role="updateUserStatus" />
            )}
          </Button>
          <Button variant="secondary" onClick={handleCancelEdit}>
            Cancel
          </Button>
        </Form.Group>
      </Form>
    </>
  );
};

export default EditUserForm;
