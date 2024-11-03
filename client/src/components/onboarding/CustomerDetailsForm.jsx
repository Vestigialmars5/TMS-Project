import React from "react";
import Form from "react-bootstrap/Form";

const CustomerDetailsForm = () => {
  const [companyName, setCompanyName] = useState("");
  const [companyAddress, setCompanyAddress] = useState("");
  const [companyNameError, setCompanyNameError] = useState("");
  const [companyAddressError, setCompanyAddressError] = useState("");

  const handleCompanyNameChange = (e) => {
    setCompanyName(e.target.value);
    setCompanyNameError(validateCompanyName(e.target.value));
  };

  const handleCompanyAddressChange = (e) => {
    setCompanyAddress(e.target.value);
    setCompanyAddressError(validateCompanyAddress(e.target.value));
  };

  const validateCompanyName = (companyName) => {
    // pass
  };

  const validateCompanyAddress = (companyAddress) => {
    // pass
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const companyNameError = validateCompanyName(companyName);
    const companyAddressError = validateCompanyAddress(companyAddress);

    if (companyNameError || companyAddressError) {
      setCompanyNameError(companyNameError);
      setCompanyAddressError(companyAddressError);
    } else {
      submitRoleDetails({ companyName, companyAddress });
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="companyName">
        <Form.Label>Company Name</Form.Label>
        <Form.Control
          type="text"
          name="companyName"
          value={companyName}
          onChange={handleCompanyNameChange}
        />
      </Form.Group>
      {companyNameError && <p>{companyNameError}</p>}
      <Form.Group controlId="companyAddress">
        <Form.Label>Company Address</Form.Label>
        <Form.Control
          type="text"
          name="companyAddress"
          value={companyAddress}
          onChange={handleCompanyAddressChange}
        />
      </Form.Group>
      {companyAddressError && <p>{companyAddressError}</p>}
    </Form>
  );
};

export default CustomerDetailsForm;
