import React from "react";
import Form from "react-bootstrap/Form"

const SearchBox = ({ searchValue, searchChange }) => {

  return (
    <Form className="mb-4">
      <Form.Group controlId="search">
        <Form.Control
          type="text"
          placeholder="Search..."
          value={searchValue}
          onChange={searchChange}
        />
      </Form.Group>
    </Form>
  );
};

export default SearchBox;
