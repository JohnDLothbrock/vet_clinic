import {
  useEffect,
  useState
} from "react";

import toast from "react-hot-toast";

import UserForm from "../components/UserForm";
import UserList from "../components/UserList";
import ConfirmModal from "../components/ConfirmModal";
import PaginationControls from "../components/PaginationControls";

import useConfirmModal from "../hooks/useConfirmModal";

import {
  getPaginatedUsers,
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
    searchTerm,
    setSearchTerm
  ] = useState("");

  const [
    roleFilter,
    setRoleFilter
  ] = useState("");

  const [
    activeFilter,
    setActiveFilter
  ] = useState("");

  const [
    page,
    setPage
  ] = useState(1);

  const [
    pageSize,
    setPageSize
  ] = useState(10);

  const [
    total,
    setTotal
  ] = useState(0);

  const [
    totalPages,
    setTotalPages
  ] = useState(0);

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

  const {
    confirmModalProps,
    openConfirmModal
  } = useConfirmModal();

  const activeUsersShown =
    users.filter(
      (user) => user.active
    ).length;

  const fetchUsers =
    async (
      pageToLoad = page,
      filtersOverride = null
    ) => {

      try {

        setLoading(true);

        const filters =
          filtersOverride || {
            search: searchTerm.trim(),
            role_id: roleFilter,
            active: activeFilter
          };

        const data =
          await getPaginatedUsers({
            page: pageToLoad,
            page_size: pageSize,
            search: filters.search,
            role_id: filters.role_id,
            active: filters.active
          });

        setUsers(
          data.items
        );

        setTotal(
          data.total
        );

        setTotalPages(
          data.total_pages
        );

        setPage(
          data.page
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

    fetchUsers(
      page
    );

  }, [
    page,
    pageSize
  ]);

  const handleSearch =
    async () => {

      setError("");

      const filters = {
        search: searchTerm.trim(),
        role_id: roleFilter,
        active: activeFilter
      };

      await fetchUsers(
        1,
        filters
      );
    };

  const handleClearFilters =
    async () => {

      setError("");

      setSearchTerm("");
      setRoleFilter("");
      setActiveFilter("");

      await fetchUsers(
        1,
        {
          search: "",
          role_id: "",
          active: ""
        }
      );
    };

  const handleSearchKeyDown =
    (event) => {

      if (event.key === "Enter") {

        handleSearch();
      }
    };

  const handlePageChange =
    (newPage) => {

      setPage(
        newPage
      );
    };

  const handlePageSizeChange =
    (newPageSize) => {

      setPageSize(
        newPageSize
      );

      setPage(1);
    };

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

        await fetchUsers(
          page
        );

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
        await openConfirmModal({
          title: "Change user role?",
          message: "This will update the permissions available to this user.",
          confirmText: "Change Role",
          cancelText: "Cancel",
          variant: "default"
        });

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

        await fetchUsers(
          page
        );

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
        await openConfirmModal({
          title: active
            ? "Activate user?"
            : "Deactivate user?",
          message: active
            ? "This user will be able to access the system again."
            : "This user will no longer be able to access the system.",
          confirmText: active
            ? "Activate User"
            : "Deactivate User",
          cancelText: "Cancel",
          variant: active
            ? "default"
            : "danger"
        });

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

        await fetchUsers(
          page
        );

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

      <ConfirmModal
        {...confirmModalProps}
      />

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
              {total}
            </span>

            <span className="page-summary-label">
              total users
            </span>

          </div>

          <div className="page-summary-card">

            <span className="page-summary-number">
              {activeUsersShown}
            </span>

            <span className="page-summary-label">
              active shown
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
              Search users, filter by role or status, and update access controls.
            </p>

          </div>

        </div>

        <div className="advanced-filter-grid">

          <input
            type="text"
            placeholder="Search username or email..."
            value={searchTerm}
            onChange={(event) => {

              setError("");

              setSearchTerm(
                event.target.value
              );

            }}
            onKeyDown={handleSearchKeyDown}
          />

          <select
            value={roleFilter}
            onChange={(event) => {

              setError("");

              setRoleFilter(
                event.target.value
              );

            }}
          >

            <option value="">
              All roles
            </option>

            <option value="1">
              Admin
            </option>

            <option value="2">
              Veterinarian
            </option>

            <option value="3">
              Receptionist
            </option>

          </select>

          <select
            value={activeFilter}
            onChange={(event) => {

              setError("");

              setActiveFilter(
                event.target.value
              );

            }}
          >

            <option value="">
              All statuses
            </option>

            <option value="true">
              Active
            </option>

            <option value="false">
              Inactive
            </option>

          </select>

          <button
            type="button"
            onClick={handleSearch}
          >
            Apply
          </button>

          <button
            type="button"
            onClick={handleClearFilters}
            className="secondary-button"
          >
            Clear
          </button>

        </div>

        {loading ? (

          <div className="loading-card">
            Loading users...
          </div>

        ) : (

          <>

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

            <PaginationControls
              page={page}
              pageSize={pageSize}
              total={total}
              totalPages={totalPages}
              onPageChange={handlePageChange}
              onPageSizeChange={handlePageSizeChange}
            />

          </>

        )}

      </div>

    </div>
  );
}

export default UsersPage;