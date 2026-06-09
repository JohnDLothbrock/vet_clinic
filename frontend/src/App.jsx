import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";

import Navbar from "./components/Navbar";
import ProtectedRoute from "./components/ProtectedRoute";

import LoginPage from "./pages/LoginPage";
import ForgotPasswordPage from "./pages/ForgotPasswordPage";
import ResetPasswordPage from "./pages/ResetPasswordPage";
import DashboardPage from "./pages/DashboardPage";
import PetsPage from "./pages/PetsPage";
import OwnersPage from "./pages/OwnersPage";
import AppointmentsPage from "./pages/AppointmentsPage";
import AuditLogsPage from "./pages/AuditLogsPage";

import {
  isAuthenticated
} from "./services/tokenService";

import {
  canViewAuditLogs
} from "./services/permissionService";

function ProtectedLayout({
  children
}) {

  return (

    <ProtectedRoute>

      <Navbar />

      {children}

    </ProtectedRoute>
  );
}

function AdminRoute({
  children
}) {

  if (!isAuthenticated()) {

    return (
      <Navigate
        to="/login"
        replace
      />
    );
  }

  if (!canViewAuditLogs()) {

    return (
      <Navigate
        to="/"
        replace
      />
    );
  }

  return (

    <>

      <Navbar />

      {children}

    </>
  );
}

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route
          path="/login"
          element={
            isAuthenticated()
              ? (
                <Navigate
                  to="/"
                  replace
                />
              )
              : (
                <LoginPage />
              )
          }
        />

        <Route
          path="/forgot-password"
          element={
            isAuthenticated()
              ? (
                <Navigate
                  to="/"
                  replace
                />
              )
              : (
                <ForgotPasswordPage />
              )
          }
        />

        <Route
          path="/reset-password"
          element={
            isAuthenticated()
              ? (
                <Navigate
                  to="/"
                  replace
                />
              )
              : (
                <ResetPasswordPage />
              )
          }
        />

        <Route
          path="/"
          element={
            <ProtectedLayout>
              <DashboardPage />
            </ProtectedLayout>
          }
        />

        <Route
          path="/pets"
          element={
            <ProtectedLayout>
              <PetsPage />
            </ProtectedLayout>
          }
        />

        <Route
          path="/owners"
          element={
            <ProtectedLayout>
              <OwnersPage />
            </ProtectedLayout>
          }
        />

        <Route
          path="/appointments"
          element={
            <ProtectedLayout>
              <AppointmentsPage />
            </ProtectedLayout>
          }
        />

        <Route
          path="/audit-logs"
          element={
            <AdminRoute>
              <AuditLogsPage />
            </AdminRoute>
          }
        />

        <Route
          path="*"
          element={
            <Navigate
              to="/"
              replace
            />
          }
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;