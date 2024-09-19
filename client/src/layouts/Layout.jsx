import React from "react";
import { Outlet } from "react-router-dom";
import AlertsContainer from "../components-new/common/AlertsContainer";

const Layout = () => {
  return (
    <div>
      <header>
        <AlertsContainer key="alerts-container" />
        <div>
          <h1>Title Here</h1>
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
