import React, { useState } from "react";
import ListGroup from "react-bootstrap/ListGroup";
import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";
import { useQuery } from "@tanstack/react-query";
import Spinner from "react-bootstrap/Spinner";
import { showAlert } from "../../../store/actions/alertsActions";
import { getOrderDetails } from "../../../services/orderService";

const OrderDetailsCard = ({ order }) => {

  const {
    data: details,
    isLoading,
    error,
  } = useQuery({
    queryKey: ["orderDetails", order.orderId],
    queryFn: () => getOrderDetails({ orderId: order.orderId }),
    enabled: !!order.orderId,
    refetchOnWindowFocus: false,
  });

  if (isLoading) {
    return <Spinner animation="border" />;
  }

  if (error) {
    const message =
      error.response?.data?.description ||
      error.response?.data?.error ||
      "An Unknown Error Occurred";
    console.error(error);
    showAlert(`Error Retrieving Details: ${message}`, "danger");
    return <p>Try again...</p>
  }

  return (
    <>
      <ListGroup horizontal>
        <ListGroup.Item>{order.referenceId}</ListGroup.Item>
        <ListGroup.Item>{order.orderId}</ListGroup.Item>
        <ListGroup.Item>{order.customerId}</ListGroup.Item>
        <ListGroup.Item>{order.total}</ListGroup.Item>
        <ListGroup.Item>{order.status}</ListGroup.Item>
        <ListGroup.Item>{order.createdAt}</ListGroup.Item>
        <ListGroup.Item>{order.updatedAt}</ListGroup.Item>
      </ListGroup>
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

      <section>
        <h4>Products</h4>
        {details?.map((product) => (
          <ListGroup.Item key={product.productId}>
            <div>
              <div>{product.productName}</div>
              <div>{product.quantity}</div>
              <div>{product.price}</div>
            </div>
          </ListGroup.Item>
        ))}
      </section>
    </>
  );
};

export default OrderDetailsCard;
