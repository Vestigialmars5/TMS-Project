import React, { useState } from "react";
import { Form, Spinner } from "react-bootstrap";
import { useAuth } from "../../hooks/useAuth";
import { useOnboarding } from "../../hooks/useOnboarding";
import Button from "react-bootstrap/Button";

const UserDetailsForm = () => {
  const { user } = useAuth();
  const { submitUserDetails, submitUserDetailsStatus } = useOnboarding();
  const email = user.email;
  const [password, setPassword] = useState("");
  const [confirmation, setConfirmation] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [address, setAddress] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [confirmationError, setConfirmationError] = useState("");
  const [firstNameError, setFirstNameError] = useState("");
  const [lastNameError, setLastNameError] = useState("");
  const [phoneNumberError, setPhoneNumberError] = useState("");
  const [addressError, setAddressError] = useState("");

  // TODO: Move validations to a separate file

  const validatePassword = (password) => {
    if (!password) {
      return "Password is required";
    } else if (password.length < 8) {
      return "Password must be at least 8 characters";
    }
    return "";
  };

  const validateConfirmation = (confirmation) => {
    // pass

  };

  const validateFirstName = (firstName) => {
    // pass
  };

  const validateLastName = (lastName) => {
    // pass
  };

  const validatePhoneNumber = (phoneNumber) => {
    // pass
  };

  const validateAddress = (address) => {
    // pass
  };


  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
    setPasswordError(validatePassword(e.target.value));
  };

  const handleConfirmationChange = (e) => {
    setConfirmation(e.target.value);
    setConfirmationError(validateConfirmation(e.target.value));
  };

  const handleFirstNameChange = (e) => {
    setFirstName(e.target.value);
    setFirstNameError(validateFirstName(e.target.value));
  };

  const handleLastNameChange = (e) => {
    setLastName(e.target.value);
    setLastNameError(validateLastName(e.target.value));
  };

  const handlePhoneNumberChange = (e) => {
    setPhoneNumber(e.target.value);
    setPhoneNumberError(validatePhoneNumber(e.target.value));
  };

  const handleAddressChange = (e) => {
    setAddress(e.target.value);
    setAddressError(validateAddress(e.target.value));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const passwordErr = validatePassword(password);
    const confirmationErr = validateConfirmation(confirmation);
    const firstNameErr = validateFirstName(firstName);
    const lastNameErr = validateLastName(lastName);
    const phoneNumberErr = validatePhoneNumber(phoneNumber);
    const addressErr = validateAddress(address);

    if (
      passwordErr ||
      confirmationErr ||
      firstNameErr ||
      lastNameErr ||
      phoneNumberErr ||
      addressErr
    ) {
      setPasswordError(passwordErr);
      setConfirmationError(confirmationErr);
      setFirstNameError(firstNameErr);
      setLastNameError(lastNameErr);
      setPhoneNumberError(phoneNumberErr);
      setAddressError(addressErr);
    } else {
      submitUserDetails({ email, password, confirmation, firstName, lastName, phoneNumber, address });
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="email">
        <Form.Label>Email</Form.Label>
        <Form.Control
          type="email"
          name="email"
          value={email}
          disabled
          readOnly
        />
      </Form.Group>

      <Form.Group controlId="password">
        <Form.Label>Password</Form.Label>
        <Form.Control
          type="password"
          name="password"
          value={password}
          onChange={handlePasswordChange}
        />
      </Form.Group>
      {passwordError && <p>{passwordError}</p>}

      <Form.Group controlId="confirmation">
        <Form.Label>Confirm Password</Form.Label>
        <Form.Control
          type="password"
          name="confirmation"
          value={confirmation}
          onChange={handleConfirmationChange}
        />
      </Form.Group>
      {confirmationError && <p>{confirmationError}</p>}

      <Form.Group controlId="firstName">
        <Form.Label>First Name</Form.Label>
        <Form.Control
          type="text"
          name="firstName"
          value={firstName}
          onChange={handleFirstNameChange}
        />
      </Form.Group>
      {firstNameError && <p>{firstNameError}</p>}

      <Form.Group controlId="lastName">
        <Form.Label>Last Name</Form.Label>
        <Form.Control
          type="text"
          name="lastName"
          value={lastName}
          onChange={handleLastNameChange}
        />
      </Form.Group>
      {lastNameError && <p>{lastNameError}</p>}

      <Form.Group controlId="phoneNumber">
        <Form.Label>Phone Number</Form.Label>
        <Form.Control
          type="tel"
          name="phoneNumber"
          pattern="[0-9]{3}[0-9]{3}[0-9]{4}"
          value={phoneNumber}
          onChange={handlePhoneNumberChange}
        />
      </Form.Group>
      {phoneNumberError && <p>{phoneNumberError}</p>}

      <Form.Group controlId="address">
        <Form.Label>Address</Form.Label>
        <Form.Control
          type="text"
          name="address"
          value={address}
          onChange={handleAddressChange}
        />
      </Form.Group>
      {addressError && <p>{addressError}</p>}
      <Button
        variant="primary"
        type="submit"
        disabled={submitUserDetailsStatus === "pending"}
      >
        {submitUserDetailsStatus !== "pending" ? (
          "Submit"
        ) : (
          <Spinner animation="border" role="submitUserDetailsStatus" />
        )}
      </Button>
    </Form>
  );
};

export default UserDetailsForm;
