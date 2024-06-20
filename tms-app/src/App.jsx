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

function App() {
  return (
    <div className="App">
      <AuthProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Layout />}>
              <Route index element={<Navigate to="/home" />} />
              <Route path="/home" element={<Home />} />

              {/* Logged out only */}
              <Route
                path="/login"
                element={<CustomRoute requiredRestriction="loggedOut" />}
              >
                <Route index element={<Login />} />
              </Route>
              {/* End logged out only */}

              {/* Private routes for admin */}
              <Route
                path="/admin"
                element={<CustomRoute requiredRole="Admin" />}
              >
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
        </BrowserRouter>
      </AuthProvider>
    </div>
  );
}

export default App;
