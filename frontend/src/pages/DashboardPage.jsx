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

        setDashboard(
          data
        );

      } catch (error) {

        console.error(
          "Error loading dashboard:",
          error
        );
      }
    };

  if (!dashboard) {

    return (

      <div className="container">

        <div className="card">

          <p>
            Loading dashboard...
          </p>

        </div>

      </div>
    );
  }

  return (

    <div className="container">

      <div className="dashboard-header">

        <div>

          <h1>
            Dashboard
          </h1>

          <p>
            Quick overview of clinic activity and recent appointments.
          </p>

        </div>

      </div>

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

          <p>
            View and manage client records.
          </p>

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

          <p>
            Track registered pets and owners.
          </p>

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

          <p>
            Review scheduled clinic visits.
          </p>

        </div>

      </div>

      <div className="card">

        <h2>
          Recent Appointments
        </h2>

        {dashboard.recent_appointments
          ?.length === 0 ? (

          <p className="empty-message">
            No appointments found.
          </p>

        ) : (

          <ul className="recent-appointments-list">

            {dashboard.recent_appointments.map(
              (appointment) => (

                <li
                  key={appointment.id}
                  className="recent-appointment-card"
                >

                  <strong>
                    {appointment.pet_name}
                  </strong>

                  <br />

                  {appointment.reason}

                </li>

              )
            )}

          </ul>

        )}

      </div>

    </div>
  );
}

export default DashboardPage;