import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Layout from "./layouts/Layout";
import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import NoPage from "./pages/no-page/NoPage";
import AdminDashboard from "./pages/admin/AdminDashboard";
import UserManagement from "./pages/admin/UserManagement";
import CustomerDashboard from "./pages/customer/CustomerDashboard";
import CustomerOrderManagement from "./pages/customer/OrderManagement";
import DispatcherDashboard from "./pages/dispatcher/DispatcherDashboard";
import DispatcherOrderManagement from "./pages/dispatcher/OrderManagement";
import "./App.css";
import Onboarding from "./pages/onboarding/Onboarding";
import PrivateRoute from "./routes/PrivateRoute";
import AdminRoute from "./routes/AdminRoute";
import CustomerRoute from "./routes/CustomerRoute";
import DispatcherRoute from "./routes/DispatcherRoute";
import PublicRoute from "./routes/PublicRoute";

function App() {
  return (
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
          <Route path="user-management" element={<UserManagement />} exact />
        </Route>
        {/* End private routes for admin */}

        {/* Private routes for customer */}
        <Route path="/customer" element={<CustomerRoute />}>
          <Route index element={<CustomerDashboard />} />
          <Route path="orders" element={<CustomerOrderManagement />} exact />
        </Route>
        {/* End private routes for customer */}

        {/* Private routes for dispatcher */}
        <Route path="/dispatcher" element={<DispatcherRoute />}>
          <Route index element={<DispatcherDashboard />} />
          <Route path="orders" element={<DispatcherOrderManagement />} exact />
        </Route>
        {/* End private routes for dispatcher */}

        <Route path="*" element={<NoPage />} />
      </Route>
    </Routes>
  );
}

export default App;
