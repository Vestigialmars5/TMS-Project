import React, { useEffect } from "react";
import { useState } from "react";
import { useAuth } from "../../context/AuthProvider";
import { Form, Button, Spinner } from "react-bootstrap";
import { onboardUserApi } from "../../utils/onboarding";
import { navigateBasedOnRole } from "../../utils/navigation";
import { useNavigate } from "react-router-dom";

const Onboarding = () => {
  const { user, updateUser, updateLoginStatus } = useAuth();
  const navigate = useNavigate();
  const [userData, setUserInfo] = useState({
    email: user.email,
    password: "********",
    confirmation: "",
    firstName: "",
    lastName: "",
    phoneNumber: "",
    address: "",
  });

  // TODO: Validations

  const handleChange = (e) => {
    setUserInfo({ ...userData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // TODO: Validations
    try {
      console.log(userData);
      const updatedUserData = await onboardUserApi({ userData });
      updateUser(updatedUserData);
      navigateBasedOnRole(user.roleName, navigate); // Doesn't modify role so safe to use original
    } catch {
      console.error("Onboarding failed");
      // TODO: Logout
    }
  };

  return (
    <>
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={userData.email}
            onChange={handleChange}
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

        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </>
  );
};

export default Onboarding;
