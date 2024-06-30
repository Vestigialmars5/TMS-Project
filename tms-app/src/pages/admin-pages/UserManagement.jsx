// Add, edit, and remove users. Assign roles and permissions.
import React, { useCallback, useEffect, useState } from "react";
import Container from "react-bootstrap/Container";
import PaginationComponent from "../../components/shared/PaginationComponent";
import SearchBox from "../../components/shared/SearchBox";
import { useUserManagement } from "../../context/UserManagementProvider";
import UsersTable from "../../components/admin/user-management/UsersTable";
import CreateUser from "../../components/admin/user-management/CreateUser";
import { debounce } from "../../utils/utils";
import { useAlert } from "../../context/AlertProvider";

const UserManagement = () => {
  const { getUsers, refresh } = useUserManagement();
  const [searchField, setSearchField] = useState("");
  const [sort, setSort] = useState("asc");
  const [page, setPage] = useState(1);
  const [limit, setLimit] = useState(10);
  const [total, setTotal] = useState(0);
  const { addAlert } = useAlert();

  useEffect(() => {
    fetchUsers();
  }, [searchField, page, refresh]);

  const fetchUsers = async () => {
    try {
      await getUsers({ searchField, sort, page, limit });
    } catch (error) {
      addAlert(error.message, "danger");
    }
  };

  const handleSearchChange = useCallback(
    debounce((e) => {
      setSearchField(e.target.value);
      setPage(1);
    }, 300),
    []
  );

  const handlePageChange = (newPage) => {
    setPage(newPage);
  };

  return (
    <Container>
      <div className="main-title-container">
        <h1>User Management</h1>
        <SearchBox searchChange={handleSearchChange} />
        {/* TODO: Create Add user component for toggling form */}
        <CreateUser />
      </div>
      <UsersTable />
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
