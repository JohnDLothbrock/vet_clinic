import {
  Link,
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import {
  logout
} from "../services/authService";

import {
  getUsername,
  getUserRoleId
} from "../services/tokenService";

import {
  canViewAuditLogs,
  canViewUsers,
  canViewMedicalRecords
} from "../services/permissionService";

function Navbar() {

  const navigate =
    useNavigate();

  const username =
    getUsername();

  const roleId =
    getUserRoleId();

  const handleLogout =
    () => {

      logout();

      toast.success(
        "Logged out successfully."
      );

      navigate(
        "/login",
        {
          replace: true
        }
      );
    };

  const getRoleName =
    () => {

      if (roleId === 1) {

        return "Admin";
      }

      if (roleId === 2) {

        return "Veterinarian";
      }

      if (roleId === 3) {

        return "Receptionist";
      }

      return "User";
    };

  return (

    <nav className="navbar">

      <div className="navbar-links">

        <Link to="/">
          Dashboard
        </Link>

        <Link to="/pets">
          Pets
        </Link>

        <Link to="/owners">
          Owners
        </Link>

        <Link to="/appointments">
          Appointments
        </Link>

        {canViewMedicalRecords() && (

          <Link to="/medical-records">
            Medical Records
          </Link>

        )}

        {canViewUsers() && (

          <Link to="/users">
            Users
          </Link>

        )}

        {canViewAuditLogs() && (

          <Link to="/audit-logs">
            Audit Logs
          </Link>

        )}

      </div>

      <div className="navbar-user">

        <span>
          {username} ({getRoleName()})
        </span>

        <Link to="/change-password">
          Change Password
        </Link>

        <button
          type="button"
          onClick={handleLogout}
          className="logout-button"
        >
          Logout
        </button>

      </div>

    </nav>
  );
}

export default Navbar;