import React, { useState } from "react";
import ListGroup from "react-bootstrap/ListGroup";
import EditUserForm from "./EditUserForm";
import Modal from "react-bootstrap/Modal";

const UserCard = ({ user }) => {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const handleEdit = () => {
    setIsEditing(true);
  };
  return (
    <>
      <ListGroup horizontal>
        <ListGroup.Item>{user.userId}</ListGroup.Item>
        <ListGroup.Item>{user.email}</ListGroup.Item>
        <ListGroup.Item>{user.roleName}</ListGroup.Item>
        <ListGroup.Item>
          <button onClick={handleShow}>Edit</button>
          <button>Delete</button>
        </ListGroup.Item>
      </ListGroup>
      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Edit User</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <EditUserForm user={user} cancelEdit={handleClose} />
        </Modal.Body>
      </Modal>
    </>
  );
};

export default UserCard;
