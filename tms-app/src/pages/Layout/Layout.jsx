import { Outlet, Link } from "react-router-dom";

const Layout = () => {
  // TODO: Make a component for this
  return (
    <>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
        </ul>
      </nav>

      <Outlet />
    </>
  );
};

export default Layout;
