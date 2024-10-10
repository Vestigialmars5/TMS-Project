import React from "react";
import { Outlet } from "react-router-dom";
import AlertsContainer from "../components/common/AlertsContainer";

const Layout = () => {
  return (
    <div>
      <header>
        <AlertsContainer key="alerts-container" />
        <div>
          <h1>Transportation Management System</h1>
          <h6>By: Jorge Emilio Peña De La Canal</h6>
        </div>
      </header>
      <main>
        <Outlet />
      </main>
      <footer>
        <p>Footer Content Here</p>
      </footer>
    </div>
  );
};

export default Layout;
