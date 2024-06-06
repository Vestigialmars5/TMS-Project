import { Outlet, Link } from "react-router-dom";
import LogoutButton from "../logout/LogoutButton";

const Layout = () => {
  // TODO: Make a component for this
  return (
    <div>
      <header>
        <nav>
          <ul>
            <li>
              <LogoutButton />
            </li>
          </ul>
        </nav>
      </header>
      <main>
        <Outlet />
      </main>
    </div>
  );
};

export default Layout;
