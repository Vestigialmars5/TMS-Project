import { Outlet } from "react-router-dom";
import LoginButton from "../login/LoginButton";
import LogoutButton from "../logout/LogoutButton";
import { useAuth } from "../../utils/auth";

const Layout = () => {
  // TODO: Finish this
  const { isLoggedIn, user } = useAuth();

  return (
    <div>
      <header>
        <nav>
          <ul>
            {isLoggedIn ? (
              <li>
                <p>
                  You Are logged in as {user.email} {user.role}{" "}
                  {isLoggedIn.toString()}
                </p>
                <LogoutButton />
              </li>
            ) : (
              <li>
                <LoginButton />
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
