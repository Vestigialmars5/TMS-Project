import React, { useState } from "react";
import CreateUserForm from "./CreateUserForm";
import { useUserManagement } from "../../../context/UserManagementProvider";

const CreateUser = () => {
  const [createUserError, setCreateUserError] = useState("");
  const {createUser} = useUserManagement();

  const hanldeCreateUser = async (userData) => {
    try {
      console.log("trying creating");
      await createUser(userData);
    } catch (error) {
      setCreateUserError(error.message);
    }
  };

  return (
    <>
      <CreateUserForm onSubmit={hanldeCreateUser} errorMessage={createUserError}/>
    </>
  );
};

export default CreateUser;
