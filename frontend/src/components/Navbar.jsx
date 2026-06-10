import {
  NavLink,
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

        <NavLink to="/">
          Dashboard
        </NavLink>

        <NavLink to="/pets">
          Pets
        </NavLink>

        <NavLink to="/owners">
          Owners
        </NavLink>

        <NavLink to="/appointments">
          Appointments
        </NavLink>

        {canViewMedicalRecords() && (

          <NavLink to="/medical-records">
            Medical Records
          </NavLink>

        )}

        {canViewUsers() && (

          <NavLink to="/users">
            Users
          </NavLink>

        )}

        {canViewAuditLogs() && (

          <NavLink to="/audit-logs">
            Audit Logs
          </NavLink>

        )}

      </div>

      <div className="navbar-user">

        <span>
          {username} · {getRoleName()}
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