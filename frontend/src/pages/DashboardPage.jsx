import {
  useEffect,
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import {
  getDashboardData
} from "../services/dashboardService";

function DashboardPage() {

  const navigate =
    useNavigate();

  const [
    dashboard,
    setDashboard
  ] = useState(null);

  useEffect(() => {

    fetchDashboard();

  }, []);

  const fetchDashboard =
    async () => {

      try {

        const data =
          await getDashboardData();

        setDashboard(data);

      } catch (error) {

        console.error(
          "Error loading dashboard:",
          error
        );
      }
    };

  if (!dashboard) {

    return (
      <p>
        Loading dashboard...
      </p>
    );
  }

  return (

    <div className="container">

      <h1>
        Dashboard
      </h1>

      <div className="dashboard-grid">

        <div
          className="dashboard-card clickable-card"
          onClick={() =>
            navigate("/owners")
          }
        >

          <h2>
            Owners
          </h2>

          <h1>
            {dashboard.total_owners}
          </h1>

        </div>

        <div
          className="dashboard-card clickable-card"
          onClick={() =>
            navigate("/pets")
          }
        >

          <h2>
            Pets
          </h2>

          <h1>
            {dashboard.total_pets}
          </h1>

        </div>

        <div
          className="dashboard-card clickable-card"
          onClick={() =>
            navigate("/appointments")
          }
        >

          <h2>
            Appointments
          </h2>

          <h1>
            {dashboard.total_appointments}
          </h1>

        </div>

      </div>

    </div>
  );
}

export default DashboardPage;