import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Layout from "./components/layout/Layout";
import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import NoPage from "./pages/no-page/NoPage";
import AdminDashboard from "./pages/admin-pages/AdminDashboard";
import CustomRoute from "./components/custom-route/CustomRoute";
import UserManagement from "./pages/admin-pages/UserManagement";
import { AuthProvider } from "./utils/AuthProvider";
import "./App.css";

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
                element={<CustomRoute requiredRole="admin" />}
              >
                <Route index element={<AdminDashboard />} />
                <Route path="user-management" element={<UserManagement />} />
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
