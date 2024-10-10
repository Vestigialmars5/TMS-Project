import React, { useState } from "react";
import ListGroup from "react-bootstrap/ListGroup";
import EditUserForm from "./EditUserForm";
import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";
import Spinner from "react-bootstrap//Spinner";
import { useUsers } from "../../hooks/useUsers";

const UserCard = ({ user }) => {
  const [showEdit, setShowEdit] = useState(false);
  const [showDelete, setShowDelete] = useState(false);
  const { deleteUser, deleteUserStatus } = useUsers();

  const handleCloseEdit = () => setShowEdit(false);
  const handleShowEdit = () => setShowEdit(true);
  const handleCloseDelete = () => setShowDelete(false);
  const handleShowDelete = () => setShowDelete(true);


  const handleDelete = () => {
    deleteUser(user.userId);
  }

  if (deleteUserStatus === "success" && showDelete) {
    setShowDelete(false);
  }

  return (
    <>
      <ListGroup horizontal>
        <ListGroup.Item>{user.userId}</ListGroup.Item>
        <ListGroup.Item>{user.email}</ListGroup.Item>
        <ListGroup.Item>{user.roleName}</ListGroup.Item>
        <ListGroup.Item>
          <Button onClick={handleShowEdit} variant="secondary">Edit</Button>
          <Button onClick={handleShowDelete} variant="danger">Delete</Button>
        </ListGroup.Item>
      </ListGroup>
      <Modal show={showEdit} onHide={handleCloseEdit} centered>
        <Modal.Header closeButton>
          <Modal.Title>Edit User</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <EditUserForm user={user} cancelEdit={handleCloseEdit} />
        </Modal.Body>
      </Modal>
      <Modal show={showDelete} onHide={handleCloseDelete} backdrop="static" keyboard={false} centered>
        <Modal.Header closeButton>
          <Modal.Title>Delete User {user.email}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>!This Action Is Irreversible!</p>
          <Button onClick={handleCloseDelete} variant="primary">Cancel</Button>
          <Button onClick={handleDelete} variant="danger" disabled={deleteUserStatus === "pending"}
          >
            {deleteUserStatus !== "pending" ? (
              "Delete"
            ) : (
              <Spinner animation="border" role="deleteStatus" size="sm"/>
            )}
          </Button>
        </Modal.Body>
      </Modal>
    </>
  );
};

export default UserCard;
