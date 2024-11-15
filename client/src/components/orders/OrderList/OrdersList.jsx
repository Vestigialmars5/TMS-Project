import React from "react";
import Tab from "react-bootstrap/Tab";

const OrdersList = () => {

  return (
    <Tab.Container id="orders-list" defaultActiveKey="#Id">
      <ListGroup horizontal>
        <ListGroup.Item action href="#Id">
          Id/Reference Number
        </ListGroup.Item>
        <ListGroup.Item action href="#CustomerId">
          Customer Id
        </ListGroup.Item>
        <ListGroup.Item action href="#Total">
          Total
        </ListGroup.Item>
        <ListGroup.Item action href="#Status">
          Status
        </ListGroup.Item>
        <ListGroup.Item action href="#Actions">
          Actions
        </ListGroup.Item>
      </ListGroup>
      <Tab.Content>
        <Tab.Pane eventKey="#Id"></Tab.Pane>
        <Tab.Pane eventKey="#Customer"></Tab.Pane>
        <Tab.Pane eventKey="#Total"></Tab.Pane>
        <Tab.Pane eventKey="#Status"></Tab.Pane>
        <Tab.Pane eventKey="#Actions"></Tab.Pane>
      </Tab.Content>
    </Tab.Container>
    /* {isLoading ? (
        <Spinner animation="border" />
      ) : error ? (
        <p>Try Again...</p>
      ) : users && users.length > 0 ? (
        users.map((user, index) => <UserCard key={index} user={user} />)
      ) : (
        <p>No Users Found</p>
      )} */
  );
};

export default OrdersList;