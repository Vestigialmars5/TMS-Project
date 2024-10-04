import React, { useState } from "react";
import ListGroup from "react-bootstrap/ListGroup";

const UserCard = ({ user }) => {
  return (
    <>
      <ListGroup horizontal>
        <ListGroup.Item>{user.userId}</ListGroup.Item>
        <ListGroup.Item>{user.email}</ListGroup.Item>
        <ListGroup.Item>{user.roleName}</ListGroup.Item>
        <ListGroup.Item>
          <button >Edit</button>
          <button >Delete</button>
        </ListGroup.Item>
      </ListGroup>
    </>
  );
};

export default UserCard;
