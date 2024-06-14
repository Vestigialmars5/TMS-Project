import React from "react";
import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/Col";

const UserCard = ({ user }) => {
  return (
    <Col sm={12} md={6} lg={4} className="mb-4">
      <Card>
        <Card.Body>
          <Card.Title>{user.username}</Card.Title>
          <Card.Text>{user.id}</Card.Text>
          <Card.Text>{user.email}</Card.Text>
          <Card.Text>{user.role}</Card.Text>
        </Card.Body>
      </Card>
    </Col>
    
  );
};

export default UserCard;
