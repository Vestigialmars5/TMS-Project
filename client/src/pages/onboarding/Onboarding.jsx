import React, { useEffect } from "react";
import { useState } from "react";
import { useAuth } from "../../context/AuthProvider";
import { useAlert } from "../../context/AlertProvider";
import { Form, Button, Spinner } from "react-bootstrap";
import { onboardUserApi } from "../../utils/onboarding";
import { navigateBasedOnRole } from "../../utils/navigation";
import { useNavigate } from "react-router-dom";

const Onboarding = () => {
  const { user, updateUser } = useAuth();
  const { addAlertOld } = useAlert();
  const navigate = useNavigate();
  const [userData, setUserData] = useState({
    email: user.email,
    password: "",
    confirmation: "",
    firstName: "",
    lastName: "",
    phoneNumber: "",
    address: "",
  });

  // TODO: Validations

  const handleChange = (e) => {
    setUserData({ ...userData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // TODO: Validations
    try {
      console.log(userData);
      const updatedUserData = await onboardUserApi({ userData });
      updateUser(updatedUserData);
      addAlertOld("Onboarding successful", "success");
      navigateBasedOnRole(user.roleName, navigate); // Onboarding does't modify role, safe to use from original user
    } catch (error) {
      addAlertOld(error.message, "danger");
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

        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </>
  );
};

export default Onboarding;
