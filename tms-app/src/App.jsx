import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Layout from "./components/layout/Layout";
import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import NoPage from "./pages/no-page/NoPage";
import AdminDashboard from "./pages/admin-pages/AdminDashboard";
import PrivateRoute from "./components/custom-routes/PrivateRoute";
import "./App.css";
import { AuthProvider } from "./utils/auth";
import RestrictedRoute from "./components/custom-routes/RestrictedRoute";

function App() {
  return (
    <div className="App">
      <AuthProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Layout />}>
              <Route index element={<Navigate to="/home" />} />
              <Route path="/home" element={<Home />} />

              {/* Start logged out only */}
              <Route
                path="/login"
                element={<RestrictedRoute requiredRestriction={"loggedOut"} />}
              >
                <Route index element={<Login />} />
              </Route>
              {/* End logged out only */}

              {/* Start private routes for admin */}
              <Route
                path="/admin"
                element={<PrivateRoute requiredRole="admin" />}
              >
                <Route index element={<AdminDashboard />} />
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
