import React from "react";
import OrderForm from "../../components/orders/CreateOrder/OrderForm";
import OrdersList from "../../components/orders/OrderList/OrdersList";

const OrderManagement = () => {
  return (
    <div>
      <h1>Order Management</h1>
      <OrderForm />
      <OrdersList />
    </div>
  );
};

export default OrderManagement;
