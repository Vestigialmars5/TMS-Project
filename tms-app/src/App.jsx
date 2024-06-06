import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Layout from "./components/layout/Layout";
import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import NoPage from "./pages/no-page/NoPage";
import AdminDashboard from "./pages/dashboard/admin/AdminDashboard";
import PrivateRoute from "./components/private-route/PrivateRoute";
import "./App.css";
import { useEffect, useState } from "react";

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [email, setEmail] = useState("");

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Navigate to="/home" />} />
            <Route
              path="/home"
              element={
                <Home
                  email={email}
                  loggedIn={loggedIn}
                  setLoggedIn={setLoggedIn}
                />
              }
            />
            <Route
              path="/login"
              element={<Login setLoggedIn={setLoggedIn} setEmail={setEmail} />}
            />
            {/* Private routes for admin */}
            <Route
              path="/admin"
              element={<PrivateRoute requiredRole="admin" />}
            >
              <Route index element={<Navigate to="admin-dashboard" />} />
              <Route path="admin-dashboard" element={<AdminDashboard />} />
            </Route>
            <Route path="*" element={<NoPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
