// Overview of system performance, key metrics, and notifications.
import React from "react";
import { useAuth } from "../../utils/AuthProvider";

const AdminDashboard = () => {
  const { isLoggedIn } = useAuth();
  return (
    <>
      <h1>Welcome to AdminDashboard</h1>
      {isLoggedIn ? (<p>logged in {isLoggedIn.toString()}</p>): <p />}
    </>
  );
};

export default AdminDashboard;
