import React from "react";
import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/Col";

const UserCard = ({ user }) => {
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
