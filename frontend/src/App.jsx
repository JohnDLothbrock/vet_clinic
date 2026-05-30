import {

  BrowserRouter,
  Routes,
  Route

} from "react-router-dom";

import Navbar from "./components/Navbar";

import DashboardPage from "./pages/DashboardPage";
import PetsPage from "./pages/PetsPage";
import OwnersPage from "./pages/OwnersPage";
import AppointmentsPage from "./pages/AppointmentsPage";

function App() {

  return (

    <BrowserRouter>

      <Navbar />

      <Routes>

        <Route
          path="/"
          element={<DashboardPage />}
        />

        <Route
          path="/pets"
          element={<PetsPage />}
        />

        <Route
          path="/owners"
          element={<OwnersPage />}
        />

        <Route
          path="/appointments"
          element={<AppointmentsPage />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;