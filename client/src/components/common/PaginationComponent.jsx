import React from "react";
import Pagination from "react-bootstrap/Pagination";

const PaginationComponent = ({ total, perPage, page, handlePageChange }) => {
  const totalPages = Math.ceil(total / perPage);

  return (
    <Pagination className="mt-4">
      {Array.from({ length: totalPages }, (_, index) => (
        <Pagination.Item
          key={index + 1}
          active={page === index + 1}
          onClick={() => handlePageChange(index + 1)}
        >
          {index + 1}
        </Pagination.Item>
      ))}
    </Pagination>
  );
};

export default PaginationComponent;
