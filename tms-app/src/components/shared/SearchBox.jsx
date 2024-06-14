import React from "react";
import Form from "react-bootstrap/Form"

const SearchBox = ({ search, handleSearchChange }) => (
  <Form className="mb-4">
    <Form.Group controlId="search">
      <Form.Control
        type="text"
        placeholder="Search users..."
        value={search}
        onChange={handleSearchChange}
      />
    </Form.Group>
  </Form>
);

export default SearchBox;
