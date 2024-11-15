import { Link, useMatch } from "react-router-dom";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import { useRoleBasedNavigation } from "../../hooks/useRoleBasedNavigation";
import { useSelector } from "react-redux";
import { useAuth } from "../../hooks/useAuth";

const NavBar = () => {
  const { goToDashboard } = useRoleBasedNavigation();
  const { isAuthenticated } = useSelector((state) => state.auth);
  const { logout } = useAuth();

  const homeMatch = useMatch("/home");
  const loginMatch = useMatch("/login");
  const adminMatch = useMatch("/admin");
  const customerMatch = useMatch("/customer");

  return (
    <Navbar expand="sm" className="bg-body-tertiary">
      <Container>
        <Navbar.Brand as={Link} to="/">
          TMS
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/" active={Boolean(homeMatch)}>
              Home
            </Nav.Link>
            {isAuthenticated ? (
              <>
                <Nav.Link
                  onClick={goToDashboard}
                  active={Boolean(adminMatch) || Boolean(customerMatch)}
                >
                  Dashboard
                </Nav.Link>
                <Nav.Link onClick={logout}>Logout</Nav.Link>
              </>
            ) : (
              <Nav.Link as={Link} to="/login" active={Boolean(loginMatch)}>
                Login
              </Nav.Link>
            )}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar;
