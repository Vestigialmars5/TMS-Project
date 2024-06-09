import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Layout from "./components/layout/Layout";
import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import NoPage from "./pages/no-page/NoPage";
import AdminDashboard from "./pages/admin-pages/AdminDashboard";
import PrivateRoute from "./components/private-route/PrivateRoute";
import "./App.css";
import { useEffect, useState } from "react";

function App() {
  return (
    <div className="App">
      <AuthProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Layout />}>
              <Route index element={<Navigate to="/home" />} />
              <Route path="/home" element={<Home />} />

              <Route path="/login" element={<Login />} />
              {/* Private routes for admin */}
              <Route
                path="/admin"
                element={<PrivateRoute requiredRole="admin" />}
              >
                <Route index element={<AdminDashboard />} />
              </Route>
              <Route path="*" element={<NoPage />} />
            </Route>
          </Routes>
        </BrowserRouter>
      </AuthProvider>
    </div>
  );
}

export default App;
