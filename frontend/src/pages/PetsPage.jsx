import {
  useEffect,
  useState
} from "react";

import toast from "react-hot-toast";

import PetForm from "../components/PetForm";
import PetList from "../components/PetList";
import ConfirmModal from "../components/ConfirmModal";
import PaginationControls from "../components/PaginationControls";

import useConfirmModal from "../hooks/useConfirmModal";

import {
  getPaginatedPetsWithOwner,
  createPet,
  updatePet,
  deletePet
} from "../services/petService";

import {
  getOwners
} from "../services/ownerService";

import {
  canCreatePet,
  canEditPet,
  canDeletePet
} from "../services/permissionService";

import "../styles/app.css";

function PetsPage() {

  const [pets, setPets] =
    useState([]);

  const [owners, setOwners] =
    useState([]);

  const [searchTerm, setSearchTerm] =
    useState("");

  const [speciesFilter, setSpeciesFilter] =
    useState("");

  const [ownerFilter, setOwnerFilter] =
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
      species: "",
      age: "",
      owner_id: ""
    });

  const [
    editingPetId,
    setEditingPetId
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

  const canShowPetForm =
    canCreatePet() ||
    canEditPet();

  const fetchPets =
    async (
      pageToLoad = page,
      filtersOverride = null
    ) => {

      try {

        setLoading(true);

        const filters =
          filtersOverride || {
            search: searchTerm.trim(),
            species: speciesFilter.trim(),
            owner_id: ownerFilter
          };

        const data =
          await getPaginatedPetsWithOwner({
            page: pageToLoad,
            page_size: pageSize,
            search: filters.search,
            species: filters.species,
            owner_id: filters.owner_id
          });

        setPets(
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
          "Error fetching pets:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setLoading(false);
      }
    };

  const fetchOwners =
    async () => {

      try {

        const data =
          await getOwners();

        setOwners(data);

      } catch (error) {

        console.error(
          "Error fetching owners:",
          error
        );

        setError(
          error.message
        );
      }
    };

  useEffect(() => {

    fetchOwners();

  }, []);

  useEffect(() => {

    fetchPets(page);

  }, [
    page,
    pageSize
  ]);

  const handleSearch =
    async () => {

      setError("");

      const filters = {
        search: searchTerm.trim(),
        species: speciesFilter.trim(),
        owner_id: ownerFilter
      };

      await fetchPets(
        1,
        filters
      );
    };

  const handleClearFilters =
    async () => {

      setError("");

      setSearchTerm("");
      setSpeciesFilter("");
      setOwnerFilter("");

      await fetchPets(
        1,
        {
          search: "",
          species: "",
          owner_id: ""
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

  const handleSubmit =
    async (event) => {

      event.preventDefault();

      if (saving) {

        return;
      }

      if (
        editingPetId &&
        !canEditPet()
      ) {

        setError(
          "You do not have permission to update pets."
        );

        return;
      }

      if (
        !editingPetId &&
        !canCreatePet()
      ) {

        setError(
          "You do not have permission to create pets."
        );

        return;
      }

      if (!formData.name.trim()) {

        setError(
          "Pet name is required."
        );

        return;
      }

      if (!formData.species.trim()) {

        setError(
          "Species is required."
        );

        return;
      }

      if (!formData.age) {

        setError(
          "Age is required."
        );

        return;
      }

      if (!formData.owner_id) {

        setError(
          "Owner is required."
        );

        return;
      }

      const payload = {
        name: formData.name.trim(),
        species: formData.species.trim(),
        age: Number(formData.age),
        owner_id: Number(formData.owner_id)
      };

      try {

        setSaving(true);

        const isEditing =
          editingPetId !== null;

        if (isEditing) {

          await updatePet(
            editingPetId,
            {
              name: payload.name,
              species: payload.species,
              age: payload.age
            }
          );

          toast.success(
            "Pet updated successfully."
          );

        } else {

          await createPet(
            payload
          );

          toast.success(
            "Pet created successfully."
          );
        }

        setError("");

        resetForm();

        await fetchPets(page);

      } catch (error) {

        console.error(
          "Error saving pet:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setSaving(false);
      }
    };

  const handleDeletePet =
    async (petId) => {

      if (!canDeletePet()) {

        setError(
          "You do not have permission to delete pets."
        );

        return;
      }

      const confirmed =
        await openConfirmModal({
          title: "Delete pet?",
          message: "This will permanently remove this pet record from the system.",
          confirmText: "Delete Pet",
          cancelText: "Keep Pet",
          variant: "danger"
        });

      if (!confirmed) {

        return;
      }

      try {

        setDeletingId(
          petId
        );

        await deletePet(
          petId
        );

        toast.success(
          "Pet deleted successfully."
        );

        setError("");

        await fetchPets(page);

      } catch (error) {

        console.error(
          "Error deleting pet:",
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

  const handleEditPet =
    (pet) => {

      if (!canEditPet()) {

        setError(
          "You do not have permission to edit pets."
        );

        return;
      }

      setEditingPetId(
        pet.id
      );

      setFormData({
        name: pet.name,
        species: pet.species,
        age: pet.age,
        owner_id: pet.owner_id
      });

      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    };

  const resetForm =
    () => {

      setEditingPetId(
        null
      );

      setFormData({
        name: "",
        species: "",
        age: "",
        owner_id: ""
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
            Pets
          </h1>

          <p className="page-subtitle">
            Manage registered pets and connect them with their owners.
          </p>

        </div>

        <div className="page-summary-card">

          <span className="page-summary-number">
            {total}
          </span>

          <span className="page-summary-label">
            total pets
          </span>

        </div>

      </div>

      {error && (

        <p className="error-message">
          {error}
        </p>

      )}

      {canShowPetForm ? (

        <div className="card">

          <PetForm
            formData={formData}
            handleChange={handleChange}
            handleSubmit={handleSubmit}
            editingPetId={editingPetId}
            resetForm={resetForm}
            owners={owners}
            saving={saving}
          />

        </div>

      ) : (

        <div className="card read-only-card">

          <h2>
            Read-only access
          </h2>

          <p>
            You can view pet records, but your role cannot create or update pets.
          </p>

        </div>

      )}

      <div className="card">

        <div className="list-header">

          <div>

            <h2>
              Pet List
            </h2>

            <p>
              Search by pet, species, or owner and browse paginated results.
            </p>

          </div>

        </div>

        <div className="advanced-filter-grid">

          <input
            type="text"
            placeholder="Search pet, species, or owner..."
            value={searchTerm}
            onChange={(event) => {
              setError("");
              setSearchTerm(
                event.target.value
              );
            }}
            onKeyDown={handleSearchKeyDown}
          />

          <input
            type="text"
            placeholder="Filter by species..."
            value={speciesFilter}
            onChange={(event) => {
              setError("");
              setSpeciesFilter(
                event.target.value
              );
            }}
            onKeyDown={handleSearchKeyDown}
          />

          <select
            value={ownerFilter}
            onChange={(event) => {
              setError("");
              setOwnerFilter(
                event.target.value
              );
            }}
          >

            <option value="">
              All owners
            </option>

            {owners.map(
              (owner) => (

                <option
                  key={owner.id}
                  value={owner.id}
                >
                  {owner.name}
                </option>

              )
            )}

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
            Loading pets...
          </div>

        ) : (

          <>

            <PetList
              pets={pets}
              editPet={handleEditPet}
              deletePet={handleDeletePet}
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

export default PetsPage;

