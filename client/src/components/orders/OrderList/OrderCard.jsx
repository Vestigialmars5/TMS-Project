import React, { useState } from "react";
import ListGroup from "react-bootstrap/ListGroup";
import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";

const OrderCard = ({ order }) => {

  return (
    <>
      <ListGroup horizontal>
        <ListGroup.Item>{order.referenceId}</ListGroup.Item>
        <ListGroup.Item>{order.customerId}</ListGroup.Item>
        <ListGroup.Item>{order.deliveryAddress}</ListGroup.Item>
        <ListGroup.Item>{order.orderProducts}</ListGroup.Item>
        <ListGroup.Item>
          <Button variant="secondary">
            Edit
          </Button>
          <Button variant="danger">
            Delete
          </Button>
        </ListGroup.Item>
      </ListGroup>
      <Modal  centered>
        <Modal.Header closeButton>
          <Modal.Title>Edit Order</Modal.Title>
        </Modal.Header>
        <Modal.Body>
        </Modal.Body>
      </Modal>
      <Modal
        backdrop="static"
        keyboard={false}
        centered
      >
        <Modal.Header closeButton>
          <Modal.Title>Delete Order {order}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>!This Action Is Irreversible!</p>
          <Button variant="primary">
            Cancel
          </Button>
          <Button
            variant="danger"
          >
          </Button>
        </Modal.Body>
      </Modal>
    </>
  );
};

export default OrderCard;
