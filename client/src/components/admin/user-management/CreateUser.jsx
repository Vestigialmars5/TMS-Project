import React, { useState } from "react";
import CreateUserForm from "./CreateUserForm";
import { useUserManagement } from "../../../context/UserManagementProvider";
import { useAlert } from "../../../context/AlertProvider";

const CreateUser = () => {
  const [createUserError, setCreateUserError] = useState("");
  const { createUser, refreshUsers } = useUserManagement();
  const { addAlert } = useAlert();

  const handleCreateUser = async (userData) => {
    try {
      await createUser(userData);
      addAlert("User Created Successfully", "success");
      await refreshUsers();
    } catch (error) {
      addAlert(error.message, "danger");
    }
  };

  return (
    <>
      <CreateUserForm
        onSubmit={handleCreateUser}
        errorMessage={createUserError}
      />
    </>
  );
};

export default CreateUser;
