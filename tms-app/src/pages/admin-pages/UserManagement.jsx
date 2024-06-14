// Add, edit, and remove users. Assign roles and permissions.
import React, { useEffect, useState } from "react";
import CreateUser from "../../components/admin/user-management/CreateUser";
import UserCard from "../../components/shared/UserCard";
import Row from "react-bootstrap/Row";
import Container from "react-bootstrap/Container";
import PaginationComponent from "../../components/shared/PaginationComponent";
import SearchBox from "../../components/shared/SearchBox";
import { useUserManagement } from "../../context/UserManagementProvider";
import Card from "react-bootstrap/Card"
import Table from "react-bootstrap/Table"

const UserManagement = () => {
  const { users, getUsers, loading } = useUserManagement();
  const [userList, setUserList] = useState([]);
  const [searchField, setSearchField] = useState("");
  const [sort, setSort] = useState("asc");
  const [page, setPage] = useState(1);
  const [limit, setLimit] = useState(10);
  const [total, setTotal] = useState(0);

  useEffect(() => {
    fetchUsers();
  }, [searchField, page]);

  const fetchUsers = async () => {
    try {
      await getUsers({ searchField, sort, page, limit });
    } catch (error) {
      console.error(error.message);
    }
  };

  const handleSearchChange = (e) => {
    setSearchField(e.target.value);
    setPage(1);
  };

  const handlePageChange = (newPage) => {
    setPage(newPage);
  };

  const UserInfo = () => {
    if (loading) {
      return <h1>Loading...</h1>;
    } else if (!loading && !users) {
      return <></>;
    }
    return (
      <Row>
        {users.map((user, index) => (
          <UserCard key={index} user={user} />
        ))}
      </Row>
    );
  };

  return (
    <Container>
      <CreateUser />
      <SearchBox search={searchField} handleSearchChange={handleSearchChange} />
      <Card style={{justifyContent:"center"}}>
        <Card.Body>
          <Table hover>
            <thead>
              <tr>
                <th className="border-bottom">Name</th>
                <th className="border-bottom">Email</th>
                <th className="border-bottom">Position</th>
                <th className="border-bottom">User Created at</th>
              </tr>
            </thead>
            <tbody></tbody>
          </Table>
        </Card.Body>
      </Card>
      <UserInfo />
      <PaginationComponent
        total={10}
        perPage={limit}
        page={page}
        handlePageChange={handlePageChange}
      />
    </Container>
  );
};

export default UserManagement;
