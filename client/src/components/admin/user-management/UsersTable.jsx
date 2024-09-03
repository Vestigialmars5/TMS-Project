import { useUserManagement } from "../../../context/UserManagementProvider";
import ListGroup from "react-bootstrap/ListGroup";
import Spinner from "react-bootstrap/Spinner";
import UserCard from "./UserCard";
import { useEffect } from "react";

const UsersTable = () => {
  const { loading, users } = useUserManagement();

  useEffect(() => {}, [users]);

  return (
    <>
      <ListGroup horizontal>
        <ListGroup.Item>Id</ListGroup.Item>
        <ListGroup.Item>Email</ListGroup.Item>
        <ListGroup.Item>Role</ListGroup.Item>
        <ListGroup.Item>Actions</ListGroup.Item>
      </ListGroup>
      {loading ? (
        <Spinner animation="border" />
      ) : (
        users.map((user, index) => <UserCard key={index} user={user} />)
      )}
    </>
  );
};

export default UsersTable;
