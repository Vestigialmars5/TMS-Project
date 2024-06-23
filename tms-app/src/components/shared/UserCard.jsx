import React, { useState } from "react";
import ListGroup from "react-bootstrap/ListGroup";
import EditUser from "../admin/user-management/EditUser";
import { useUserManagement } from "../../context/UserManagementProvider";

const UserCard = ({ user }) => {
  const { deleteUser, refreshUsers } = useUserManagement();
  const [isEditing, setIsEditing] = useState(false);

  const handleDeleteUser = async () => {
    console.log("Delete user by id", user.userId);
    // TODO: Make it better Confirm dialog
    const confirmDelete = window.confirm(
      "Are you sure you want to delete this user?"
    );
    if (confirmDelete) {
      try {
        await deleteUser(user.userId);
        await refreshUsers();
      } catch (error) {
        console.error(error.message);
      }
    }
  };

  const handleEdit = () => {
    console.log("Edit user by id", user.userId);
    setIsEditing(true);
  };

  const cancelEdit = () => {
    console.log("Canceled edit");
    setIsEditing(false);
  };

  return (
    <>
      {isEditing && <EditUser user={user} cancelEdit={cancelEdit} />}
      <ListGroup horizontal>
        <ListGroup.Item>{user.username}</ListGroup.Item>
        <ListGroup.Item>{user.userId}</ListGroup.Item>
        <ListGroup.Item>{user.email}</ListGroup.Item>
        <ListGroup.Item>{user.roleName}</ListGroup.Item>
        <ListGroup.Item>
          <button onClick={handleEdit}>Edit</button>
          <button onClick={handleDeleteUser}>Delete</button>
        </ListGroup.Item>
      </ListGroup>
    </>
  );
};

export default UserCard;
