import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Layout from "./components/layout/Layout";
import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import NoPage from "./pages/no-page/NoPage";
import AdminDashboard from "./pages/admin-pages/AdminDashboard";
import CustomRoute from "./components/custom-route/CustomRoute";
import UserManagement from "./pages/admin-pages/UserManagement";
import { AuthProvider } from "./context/AuthProvider";
import { UserManagementProvider } from "./context/UserManagementProvider";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Onboarding from "./pages/onboarding/Onboarding";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <AuthProvider>
          <Routes>
            <Route path="/" element={<Layout />}>
              <Route index element={<Navigate to="/home" />} />
              <Route path="/home" element={<Home />} />

              {/* Logged out only */}
              <Route
                path="/login"
                element={<CustomRoute requiredRestrictions={["loggedOut"]} />}
              >
                <Route index element={<Login />} />
              </Route>
              {/* End logged out only */}

              {/* Authenticated not logged in only, any user */}
              <Route
                path="/onboarding"
                element={
                  <CustomRoute
                    requiredRestrictions={["loggedIn", "notOnboarded"]}
                  />
                }
              >
                <Route index element={<Onboarding />} />
              </Route>
              {/* End authenticated not logged in only, any user */}

              {/* Private routes for admin */}
              <Route path="/admin" element={<CustomRoute requiredRoleId={1} />}>
                <Route
                  index
                  element={
                    <UserManagementProvider>
                      <AdminDashboard />
                    </UserManagementProvider>
                  }
                />
                <Route
                  path="user-management"
                  element={
                    <UserManagementProvider>
                      <UserManagement />
                    </UserManagementProvider>
                  }
                />
              </Route>
              {/* End private routes for admin */}

              <Route path="*" element={<NoPage />} />
            </Route>
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
