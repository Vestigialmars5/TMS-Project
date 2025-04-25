import { useQuery } from "@tanstack/react-query";
import React, { useState, useCallback } from "react";
import ListGroup from "react-bootstrap/ListGroup";
import { getUsers } from "../../services/usersService";
import { showAlert } from "../../store/actions/alertsActions";
import Tab from "react-bootstrap/Tab";
import { debounce } from "../../utils/utils";
import Spinner from "react-bootstrap/Spinner";
import SearchBox from "../../components/common/SearchBox";
import UserCard from "./UserCard";

const UsersList = () => {
  const [searchField, setSearchField] = useState("");
  const [sortOrder, setSortOrder] = useState("asc");
  const [sortBy, setSortBy] = useState("email");
  const [page, setPage] = useState(1);
  const [limit, setLimit] = useState(10);
  const [total, setTotal] = useState(0);

  const {
    data: users,
    status: usersStatus,
    error,
  } = useQuery({
    queryKey: ["users", searchField, sortBy, sortOrder, page, limit],
    queryFn: () => getUsers({ searchField, sortBy, sortOrder, page, limit }),
    keepPreviousData: true,
    staleTime: 1000 * 60 * 5, // 5 minutes
  });

  const handleSearchChange = useCallback(
    debounce((e) => {
      setSearchField(e.target.value);
      setPage(1);
    }, 300),
    []
  );

  if (error) {
    const message =
      error.response?.data?.description ||
      error.response?.data?.error ||
      "An Unknown Error Occurred";
    console.error(error);
    showAlert(`Error Retrieving Users: ${message}`, "danger");
  }

  // TODO: Implement Pagination
  // TODO: Implement Sorting
  return (
    <div>
      <SearchBox searchChange={handleSearchChange} />
      <Tab.Container id="users-list" defaultActiveKey="#Id">
        <ListGroup horizontal>
          <ListGroup.Item action href="#Id">
            Id
          </ListGroup.Item>
          <ListGroup.Item action href="#Email">
            Email
          </ListGroup.Item>
          <ListGroup.Item action href="#Role">
            Role
          </ListGroup.Item>
          <ListGroup.Item action href="#Actions">
            Actions
          </ListGroup.Item>
        </ListGroup>
        <Tab.Content>
          <Tab.Pane eventKey="#Id"></Tab.Pane>
          <Tab.Pane eventKey="#Email"></Tab.Pane>
          <Tab.Pane eventKey="#Role"></Tab.Pane>
          <Tab.Pane eventKey="#Actions"></Tab.Pane>
        </Tab.Content>
      </Tab.Container>
      {usersStatus === "pending" ? (
        <Spinner animation="border" role="status"/>
      ) : error ? (
        <p>Try Again...</p>
      ) : users && users.length > 0 ? (
        users.map((user, index) => <UserCard key={index} user={user} />)
      ) : (
        <p>No Users Found</p>
      )}
    </div>
  );
};

export default UsersList;
