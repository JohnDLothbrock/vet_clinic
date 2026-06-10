import {
  useEffect,
  useState
} from "react";

import toast from "react-hot-toast";

import UserForm from "../components/UserForm";
import UserList from "../components/UserList";

import {
  getUsers,
  createUser,
  updateUserRole,
  updateUserActive
} from "../services/userService";

import "../styles/app.css";

function UsersPage() {

  const [
    users,
    setUsers
  ] = useState([]);

  const [
    formData,
    setFormData
  ] = useState({
    username: "",
    email: "",
    password: "",
    role_id: ""
  });

  const [
    loading,
    setLoading
  ] = useState(true);

  const [
    saving,
    setSaving
  ] = useState(false);

  const [
    updatingId,
    setUpdatingId
  ] = useState(null);

  const [
    error,
    setError
  ] = useState("");

  const activeUsers =
    users.filter(
      (user) => user.active
    ).length;

  const fetchUsers =
    async () => {

      try {

        setLoading(true);

        const data =
          await getUsers();

        setUsers(
          data
        );

        setError("");

      } catch (error) {

        console.error(
          "Error fetching users:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setLoading(false);
      }
    };

  useEffect(() => {

    fetchUsers();

  }, []);

  const handleChange =
    (event) => {

      setError("");

      setFormData({
        ...formData,
        [event.target.name]:
          event.target.value
      });
    };

  const resetForm =
    () => {

      setFormData({
        username: "",
        email: "",
        password: "",
        role_id: ""
      });
    };

  const handleSubmit =
    async (event) => {

      event.preventDefault();

      if (saving) {

        return;
      }

      if (!formData.username.trim()) {

        setError(
          "Username is required."
        );

        return;
      }

      if (!formData.email.trim()) {

        setError(
          "Email is required."
        );

        return;
      }

      if (!formData.password.trim()) {

        setError(
          "Password is required."
        );

        return;
      }

      if (formData.password.length < 8) {

        setError(
          "Password must contain at least 8 characters."
        );

        return;
      }

      if (!formData.role_id) {

        setError(
          "Role is required."
        );

        return;
      }

      try {

        setSaving(true);

        await createUser({
          username: formData.username.trim(),
          email: formData.email.trim(),
          password: formData.password,
          role_id: Number(formData.role_id)
        });

        toast.success(
          "User created successfully."
        );

        setError("");

        resetForm();

        await fetchUsers();

      } catch (error) {

        console.error(
          "Error creating user:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setSaving(false);
      }
    };

  const handleRoleChange =
    async (
      userId,
      roleId
    ) => {

      const confirmed =
        window.confirm(
          "Are you sure you want to change this user's role?"
        );

      if (!confirmed) {

        return;
      }

      try {

        setUpdatingId(
          userId
        );

        await updateUserRole(
          userId,
          roleId
        );

        toast.success(
          "User role updated successfully."
        );

        await fetchUsers();

      } catch (error) {

        console.error(
          "Error updating user role:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setUpdatingId(
          null
        );
      }
    };

  const handleActiveChange =
    async (
      userId,
      active
    ) => {

      const confirmed =
        window.confirm(
          active
            ? "Activate this user?"
            : "Deactivate this user?"
        );

      if (!confirmed) {

        return;
      }

      try {

        setUpdatingId(
          userId
        );

        await updateUserActive(
          userId,
          active
        );

        toast.success(
          "User status updated successfully."
        );

        await fetchUsers();

      } catch (error) {

        console.error(
          "Error updating user status:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setUpdatingId(
          null
        );
      }
    };

  return (

    <div className="container">

      <div className="page-header">

        <div>

          <h1 className="title">
            Users
          </h1>

          <p className="page-subtitle">
            Manage staff accounts, access roles, and active user status.
          </p>

        </div>

        <div className="users-summary-grid">

          <div className="page-summary-card">

            <span className="page-summary-number">
              {users.length}
            </span>

            <span className="page-summary-label">
              total users
            </span>

          </div>

          <div className="page-summary-card">

            <span className="page-summary-number">
              {activeUsers}
            </span>

            <span className="page-summary-label">
              active users
            </span>

          </div>

        </div>

      </div>

      {error && (

        <p className="error-message">
          {error}
        </p>

      )}

      <div className="card">

        <UserForm
          formData={formData}
          handleChange={handleChange}
          handleSubmit={handleSubmit}
          saving={saving}
        />

      </div>

      <div className="card">

        <div className="list-header">

          <div>

            <h2>
              User List
            </h2>

            <p>
              Review users, update roles, and activate or deactivate accounts.
            </p>

          </div>

        </div>

        {loading ? (

          <div className="loading-card">
            Loading users...
          </div>

        ) : (

          <UserList
            users={users}
            updatingId={updatingId}
            handleRoleChange={
              handleRoleChange
            }
            handleActiveChange={
              handleActiveChange
            }
          />

        )}

      </div>

    </div>
  );
}

export default UsersPage;