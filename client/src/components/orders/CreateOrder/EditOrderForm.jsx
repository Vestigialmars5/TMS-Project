import React from "react";
import Form from "react-bootstrap/Form";

const EditOrderForm = () => {
  return (
    <>
      <Form onSubmit={handleEditOrder}>
        <Form.Group controlId="orderId">
          <Form.Label>Id/Reference Number</Form.Label>
          <Form.Control
            type="orderId"
            defaultValue={orderId}
            onChange={handleOrderIdChange}
            autoFocus
          />
          {orderIdError && <p>{orderIdError}</p>}
        </Form.Group>

        <Form.Group controlId="customerId">
          <Form.Label>Customer Id</Form.Label>
          <Form.Control
            type="customerId"
            defaultValue={customerId}
            onChange={handleCustomerIdChange}
          />
          {customerIdError && <p>{customerIdError}</p>}
        </Form.Group>

        <Form.Group controlId="total">
          <Form.Label>Total</Form.Label>
          <Form.Control
            type="total"
            defaultValue={total}
            onChange={handleTotalChange}
          />
          {totalError && <p>{totalError}</p>}
        </Form.Group>

        <Form.Group controlId="status">
          <Form.Label>Status</Form.Label>
          <Form.Control
            type="status"
            defaultValue={status}
            onChange={handleStatusChange}
          />
          {statusError && <p>{statusError}</p>}
        </Form.Group>
      </Form>
    </>
  );
};
