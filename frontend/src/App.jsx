import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";

import Navbar from "./components/Navbar";
import ProtectedRoute from "./components/ProtectedRoute";

import LoginPage from "./pages/LoginPage";
import DashboardPage from "./pages/DashboardPage";
import PetsPage from "./pages/PetsPage";
import OwnersPage from "./pages/OwnersPage";
import AppointmentsPage from "./pages/AppointmentsPage";

import {
  isAuthenticated
} from "./services/tokenService";

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