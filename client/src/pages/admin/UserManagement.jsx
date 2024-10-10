import React from "react";
import UsersForm from "../../components/user-management/UsersForm";
import UsersList from "../../components/user-management/UsersList";

const UserManagement = () => {
  return (
    <div>
      <h1>User Management</h1>
      <UsersForm />
      <UsersList />
    </div>
  );
};

export default UserManagement;
