import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { useUserManagement } from "../../../context/UserManagementProvider";
import { useState, useEffect } from "react";
import { useAlert } from "../../../context/AlertProvider";

const EditUser = ({ user, cancelEdit }) => {
  const { updateUser, refreshUsers, getRoles, roles } = useUserManagement();
  const [email, setEmail] = useState(user.email);
  const [roleId, setRoleId] = useState(user.roleId);
  const [roleName, setRoleName] = useState(user.roleName);
  const [userId, setUserId] = useState(user.userId);
  const [emailError, setEmailError] = useState("");
  const [roleError, setRoleError] = useState("");
  const { addAlertOld } = useAlert();

  useEffect(() => {
    if (roles.length === 0) {
      getRoles();
    }
  }, []);

  const handleCancelEdit = () => {
    cancelEdit();
    addAlertOld("Edit Cancelled", "info");
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
      try {
        await updateUser({ userId, email, roleId });
        await refreshUsers();
        addAlertOld("Update Successful", "success");
        cancelEdit();
      } catch (error) {
        if (error.message == "No Changes Made") {
          addAlertOld("Update Cancelled: No Changes Made", "info");
          cancelEdit();
        } else {
          addAlertOld(error.message, "danger");
        }
      }
    }
  };

  return (
    <div>
      <h1>Edit User</h1>
      <Form onSubmit={handleEditUser}>
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
          <Form.Control as="select" value={roleId} onChange={handleRoleChange}>
            {roles.map((role, index) => (
              <option key={index} value={role.roleId}>
                {role.roleName}
              </option>
            ))}
          </Form.Control>
          {roleError && <p>{roleError}</p>}
        </Form.Group>

        <Button variant="primary" type="submit">
          Save
        </Button>
        <Button variant="secondary" type="button" onClick={handleCancelEdit}>
          Cancel
        </Button>
      </Form>
    </div>
  );
};

export default EditUser;
