import React, { useState } from "react";
import ListGroup from "react-bootstrap/ListGroup";
import EditUser from "./EditUser";
import { useUserManagement } from "../../../context/UserManagementProvider";

const UserCard = ({ user }) => {
  const { deleteUser, refreshUsers } = useUserManagement();
  const [isEditing, setIsEditing] = useState(false);

  const handleDeleteUser = async () => {
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
    setIsEditing(true);
  };

  const cancelEdit = () => {
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
