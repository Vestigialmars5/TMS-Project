import React, { useState } from "react";
import ListGroup from "react-bootstrap/ListGroup";
import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";
import { useQuery } from "@tanstack/react-query";
import OrderDetailsCard from "./OrderDetailsCard";

const OrderCard = ({ order }) => {
  const [showDetails, setShowDetails] = useState(false);

  const handleShowDetails = () => setShowDetails(true);
  const handleCloseDetails = () => setShowDetails(false);


  return (
    <>
      <ListGroup horizontal>
        <ListGroup.Item>{order.orderId}</ListGroup.Item>
        <ListGroup.Item>{order.customerId}</ListGroup.Item>
        <ListGroup.Item>{order.total}</ListGroup.Item>
        <ListGroup.Item>{order.status}</ListGroup.Item>
        <ListGroup.Item>
          <Button variant="secondary" onClick={handleShowDetails}>
            All Details
          </Button>
        </ListGroup.Item>
      </ListGroup>
      <Modal show={showDetails} onHide={handleCloseDetails} centered>
        <Modal.Header closeButton>
          <Modal.Title>Order Details</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <OrderDetailsCard order={order}/>
        </Modal.Body>
      </Modal>
      <Modal centered>
        <Modal.Header closeButton>
          <Modal.Title>Edit Order</Modal.Title>
        </Modal.Header>
        <Modal.Body></Modal.Body>
      </Modal>
      <Modal backdrop="static" keyboard={false} centered>
        <Modal.Header closeButton>
          <Modal.Title>Delete Order {order}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>!This Action Is Irreversible!</p>
          <Button variant="primary">Cancel</Button>
          <Button variant="danger"></Button>
        </Modal.Body>
      </Modal>
    </>
  );
};

export default OrderCard;
