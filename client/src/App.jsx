import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Layout from "./components/layout/Layout";
import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import NoPage from "./pages/no-page/NoPage";
import AdminDashboard from "./pages-new/admin/AdminDashboard";
import CustomRoute from "./components/custom-route/CustomRoute";
import UserManagement from "./pages/admin-pages/UserManagement";
import { AuthProvider } from "./context/AuthProvider";
import { UserManagementProvider } from "./context/UserManagementProvider";
import { AlertProvider } from "./context/AlertProvider";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Onboarding from "./pages/onboarding/Onboarding";
import PrivateRoute from "./routes/PrivateRoute";
import AdminRoute from "./routes/AdminRoute";
import PublicRoute from "./routes/PublicRoute";
import { Provider, useSelector } from "react-redux";
import { store } from "./store/index";

function App() {

  return (
    <BrowserRouter>
      <Provider store={store}>
        <AuthProvider>
          <AlertProvider>
            <Routes>
              <Route path="/" element={<Layout />}>
                <Route index element={<Navigate to="/home" />} />
                <Route path="/home" element={<Home />} />

                {/* Logged out only */}
                <Route path="/login" element={<PublicRoute />}>
                  <Route index element={<Login />} />
                </Route>
                {/* End logged out only */}

                {/* Authenticated not logged in only, any user */}
                <Route
                  path="/onboarding"
                  element={<PrivateRoute required={["not_onboarded"]} />}
                >
                  <Route index element={<Onboarding />} />
                </Route>
                {/* End authenticated not logged in only, any user */}

                {/* Private routes for admin */}
                <Route path="/admin" element={<AdminRoute />}>
                  <Route index element={<AdminDashboard />} />
                  <Route
                    path="user-management"
                    element={<UserManagement />}
                    exact
                  />
                </Route>
                {/* End private routes for admin */}

                <Route path="*" element={<NoPage />} />
              </Route>
            </Routes>
          </AlertProvider>
        </AuthProvider>
      </Provider>
    </BrowserRouter>
  );
}

export default App;
