import React, { useState } from "react";
import { Form, Spinner } from "react-bootstrap";
import { useOnboarding } from "../../hooks/useOnboarding";

const UserDetailsForm = () => {
  const { submitDetails, status } = useOnboarding();
  const [userData, setUserData] = useState({
    email: user.email,
    password: "",
    confirmation: "",
    firstName: "",
    lastName: "",
    phoneNumber: "",
    address: "",
  });

  const handleChange = (e) => {
    setUserData({ ...userData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    // TODO: Validations
    e.preventDefault();
    submitDetails(userData);
  };


  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="email">
        <Form.Label>Email</Form.Label>
        <Form.Control
          type="email"
          name="email"
          value={userData.email}
          readOnly
        />
      </Form.Group>

      <Form.Group controlId="password">
        <Form.Label>Password</Form.Label>
        <Form.Control
          type="password"
          name="password"
          value={userData.password}
          onChange={handleChange}
        />
      </Form.Group>

      <Form.Group controlId="confirmation">
        <Form.Label>Confirm Password</Form.Label>
        <Form.Control
          type="password"
          name="confirmation"
          value={userData.confirmation}
          onChange={handleChange}
        />
      </Form.Group>
      <Form.Group controlId="firstName">
        <Form.Label>First Name</Form.Label>
        <Form.Control
          type="text"
          name="firstName"
          value={userData.firstName}
          onChange={handleChange}
        />
      </Form.Group>

      <Form.Group controlId="lastName">
        <Form.Label>Last Name</Form.Label>
        <Form.Control
          type="text"
          name="lastName"
          value={userData.lastName}
          onChange={handleChange}
        />
      </Form.Group>

      <Form.Group controlId="phoneNumber">
        <Form.Label>Phone Number</Form.Label>
        <Form.Control
          type="tel"
          name="phoneNumber"
          pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
          value={userData.phoneNumber}
          onChange={handleChange}
        />
      </Form.Group>

      <Form.Group controlId="address">
        <Form.Label>Address</Form.Label>
        <Form.Control
          type="text"
          name="address"
          value={userData.address}
          onChange={handleChange}
        />
      </Form.Group>

      {status !== "loading" ? (
        <button type="submit" disabled={status === "loading"}>
          Login
        </button>
      ) : (
        <Spinner animation="border" role="status" />
      )}
    </Form>
  );
};

export default UserDetailsForm;
