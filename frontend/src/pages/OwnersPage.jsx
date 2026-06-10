import {
  useEffect,
  useState
} from "react";

import toast from "react-hot-toast";

import OwnerForm from "../components/OwnerForm";
import OwnerList from "../components/OwnerList";

import {
  getOwners,
  searchOwners,
  createOwner,
  updateOwner,
  deleteOwner
} from "../services/ownerService";

import {
  canCreateOwner,
  canEditOwner,
  canDeleteOwner
} from "../services/permissionService";

import "../styles/app.css";

function OwnersPage() {

  const [owners, setOwners] =
    useState([]);

  const [searchTerm, setSearchTerm] =
    useState("");

  const [formData, setFormData] =
    useState({
      name: "",
      phone: ""
    });

  const [
    editingOwnerId,
    setEditingOwnerId
  ] = useState(null);

  const [
    loading,
    setLoading
  ] = useState(true);

  const [
    saving,
    setSaving
  ] = useState(false);

  const [
    deletingId,
    setDeletingId
  ] = useState(null);

  const [
    error,
    setError
  ] = useState("");

  const canShowOwnerForm =
    canCreateOwner() ||
    canEditOwner();

  const fetchOwners =
    async () => {

      try {

        setLoading(true);

        const data =
          await getOwners();

        setOwners(data);

        setError("");

      } catch (error) {

        console.error(
          "Error fetching owners:",
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

    fetchOwners();

  }, []);

  const handleSearch =
    async () => {

      setError("");

      if (!searchTerm.trim()) {

        fetchOwners();

        return;
      }

      try {

        setLoading(true);

        const data =
          await searchOwners(
            searchTerm
          );

        setOwners(data);

      } catch (error) {

        console.error(
          "Error searching owners:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setLoading(false);
      }
    };

  const handleSearchKeyDown =
    (event) => {

      if (event.key === "Enter") {

        handleSearch();
      }
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

  const handleSubmit =
    async (event) => {

      event.preventDefault();

      if (saving) {

        return;
      }

      if (
        editingOwnerId &&
        !canEditOwner()
      ) {

        setError(
          "You do not have permission to update owners."
        );

        return;
      }

      if (
        !editingOwnerId &&
        !canCreateOwner()
      ) {

        setError(
          "You do not have permission to create owners."
        );

        return;
      }

      if (!formData.name.trim()) {

        setError(
          "Owner name is required."
        );

        return;
      }

      if (!formData.phone.trim()) {

        setError(
          "Phone is required."
        );

        return;
      }

      const payload = {
        name: formData.name.trim(),
        phone: formData.phone.trim()
      };

      try {

        setSaving(true);

        if (editingOwnerId) {

          await updateOwner(
            editingOwnerId,
            payload
          );

          toast.success(
            "Owner updated successfully."
          );

        } else {

          await createOwner(
            payload
          );

          toast.success(
            "Owner created successfully."
          );
        }

        setError("");

        resetForm();

        await fetchOwners();

      } catch (error) {

        console.error(
          "Error saving owner:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setSaving(false);
      }
    };

  const handleDeleteOwner =
    async (ownerId) => {

      if (!canDeleteOwner()) {

        setError(
          "You do not have permission to delete owners."
        );

        return;
      }

      const confirmed =
        window.confirm(
          "Are you sure you want to delete this owner?"
        );

      if (!confirmed) {

        return;
      }

      try {

        setDeletingId(
          ownerId
        );

        await deleteOwner(
          ownerId
        );

        toast.success(
          "Owner deleted successfully."
        );

        setError("");

        await fetchOwners();

      } catch (error) {

        console.error(
          "Error deleting owner:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setDeletingId(
          null
        );
      }
    };

  const handleEditOwner =
    (owner) => {

      if (!canEditOwner()) {

        setError(
          "You do not have permission to edit owners."
        );

        return;
      }

      setEditingOwnerId(
        owner.id
      );

      setFormData({
        name: owner.name,
        phone: owner.phone
      });

      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    };

  const resetForm =
    () => {

      setEditingOwnerId(
        null
      );

      setFormData({
        name: "",
        phone: ""
      });
    };

  return (

    <div className="container">

      <div className="page-header">

        <div>

          <h1 className="title">
            Owners
          </h1>

          <p className="page-subtitle">
            Manage client contact information and owner records.
          </p>

        </div>

        <div className="page-summary-card">

          <span className="page-summary-number">
            {owners.length}
          </span>

          <span className="page-summary-label">
            owners shown
          </span>

        </div>

      </div>

      {error && (

        <p className="error-message">
          {error}
        </p>

      )}

      {canShowOwnerForm ? (

        <div className="card">

          <OwnerForm
            formData={formData}
            handleChange={handleChange}
            handleSubmit={handleSubmit}
            editingOwnerId={editingOwnerId}
            resetForm={resetForm}
            saving={saving}
          />

        </div>

      ) : (

        <div className="card read-only-card">

          <h2>
            Read-only access
          </h2>

          <p>
            You can view owner records, but your role cannot create or update owners.
          </p>

        </div>

      )}

      <div className="card">

        <div className="list-header">

          <div>

            <h2>
              Owner List
            </h2>

            <p>
              Search by owner name or browse all registered clients.
            </p>

          </div>

        </div>

        <div className="search-bar">

          <input
            type="text"
            placeholder="Search owner by name..."
            value={searchTerm}
            onChange={(event) => {

              setError("");

              setSearchTerm(
                event.target.value
              );

            }}
            onKeyDown={handleSearchKeyDown}
          />

          <button
            type="button"
            onClick={handleSearch}
          >
            Search
          </button>

          <button
            type="button"
            onClick={() => {

              setError("");

              setSearchTerm("");

              fetchOwners();
            }}
            className="secondary-button"
          >
            Clear
          </button>

        </div>

        {loading ? (

          <div className="loading-card">
            Loading owners...
          </div>

        ) : (

          <OwnerList
            owners={owners}
            editOwner={handleEditOwner}
            deleteOwner={handleDeleteOwner}
            deletingId={deletingId}
          />

        )}

      </div>

    </div>
  );
}

export default OwnersPage;