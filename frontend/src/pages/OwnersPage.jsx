import {
  useEffect,
  useState
} from "react";

import toast from "react-hot-toast";

import OwnerForm from "../components/OwnerForm";
import OwnerList from "../components/OwnerList";
import ConfirmModal from "../components/ConfirmModal";
import PaginationControls from "../components/PaginationControls";

import useConfirmModal from "../hooks/useConfirmModal";

import {
  getPaginatedOwners,
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

  const [page, setPage] =
    useState(1);

  const [pageSize, setPageSize] =
    useState(10);

  const [total, setTotal] =
    useState(0);

  const [totalPages, setTotalPages] =
    useState(0);

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

  const {
    confirmModalProps,
    openConfirmModal
  } = useConfirmModal();

  const canShowOwnerForm =
    canCreateOwner() ||
    canEditOwner();

  const fetchOwners =
    async (
      pageToLoad = page,
      searchOverride = null
    ) => {

      try {

        setLoading(true);

        const data =
          await getPaginatedOwners({
            page: pageToLoad,
            page_size: pageSize,
            search:
              searchOverride !== null
                ? searchOverride
                : searchTerm.trim()
          });

        setOwners(
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

    fetchOwners(page);

  }, [
    page,
    pageSize
  ]);

  const handleSearch =
    async () => {

      setError("");

      const searchValue =
        searchTerm.trim();

      await fetchOwners(
        1,
        searchValue
      );
    };

  const handleClearFilters =
    async () => {

      setError("");

      setSearchTerm("");

      await fetchOwners(
        1,
        ""
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

        await fetchOwners(page);

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
        await openConfirmModal({
          title: "Delete owner?",
          message: "This will permanently remove this owner record from the system.",
          confirmText: "Delete Owner",
          cancelText: "Keep Owner",
          variant: "danger"
        });

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

        await fetchOwners(page);

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

      <ConfirmModal
        {...confirmModalProps}
      />

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
            {total}
          </span>

          <span className="page-summary-label">
            total owners
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
              Search owners by name or phone and browse paginated results.
            </p>

          </div>

        </div>

        <div className="search-bar">

          <input
            type="text"
            placeholder="Search owner by name or phone..."
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
            onClick={handleClearFilters}
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

          <>

            <OwnerList
              owners={owners}
              editOwner={handleEditOwner}
              deleteOwner={handleDeleteOwner}
              deletingId={deletingId}
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

export default OwnersPage;