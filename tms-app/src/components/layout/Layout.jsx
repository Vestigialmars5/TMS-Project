import { Outlet } from "react-router-dom";
import LogoutButton from "../logout/LogoutButton";
import { useAuth } from "../../utils/auth";

const Layout = () => {
  // TODO: Finish this
  const { isLoggedIn } = useAuth();

  return (
    <div>
      <header>
        <nav>
          <ul>
            {isLoggedIn &&(
              <li>
                <LogoutButton />
              </li>
            )}
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
