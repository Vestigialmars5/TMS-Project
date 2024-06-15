import React from "react";
import ListGroup from "react-bootstrap/ListGroup";
import { useUserManagement } from "../../context/UserManagementProvider";

const UserCard = ({ user }) => {
  const { deleteUser } = useUserManagement();

  const handleUserDelete = async () => {
    console.log("Delete user by id", user.id);
    try {
      await deleteUser(user.id);
    } catch (error) {
      console.error(error.message);
    }
  };

  const handleUserEdit = () => {
    console.log("Edit user");
  };

  return (
    <>
      {user ? (
        <ListGroup horizontal>
          <ListGroup.Item>{user.username}</ListGroup.Item>
          <ListGroup.Item>{user.id}</ListGroup.Item>
          <ListGroup.Item>{user.email}</ListGroup.Item>
          <ListGroup.Item>{user.role}</ListGroup.Item>
          <ListGroup.Item>
            <button onClick={handleUserEdit}>Edit</button>
            <button onClick={handleUserDelete}>Delete</button>
          </ListGroup.Item>
        </ListGroup>
      ) : (
        <ListGroup horizontal>
          <ListGroup.Item>Username</ListGroup.Item>
          <ListGroup.Item>Id</ListGroup.Item>
          <ListGroup.Item>Email</ListGroup.Item>
          <ListGroup.Item>Role</ListGroup.Item>
          <ListGroup.Item>Actions</ListGroup.Item>
        </ListGroup>
      )}
    </>
  );
};

export default UserCard;
