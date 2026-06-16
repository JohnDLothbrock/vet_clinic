import {
  useEffect,
  useState
} from "react";

import toast from "react-hot-toast";

import MedicalRecordForm from "../components/MedicalRecordForm";
import MedicalRecordList from "../components/MedicalRecordList";
import ConfirmModal from "../components/ConfirmModal";
import PaginationControls from "../components/PaginationControls";

import useConfirmModal from "../hooks/useConfirmModal";

import {
  getPaginatedMedicalRecords,
  createMedicalRecord,
  updateMedicalRecord,
  deleteMedicalRecord
} from "../services/medicalRecordService";

import {
  getPetsWithOwner
} from "../services/petService";

import {
  canCreateMedicalRecord,
  canEditMedicalRecord,
  canDeleteMedicalRecord
} from "../services/permissionService";

import "../styles/app.css";

function MedicalRecordsPage() {

  const [
    medicalRecords,
    setMedicalRecords
  ] = useState([]);

  const [
    pets,
    setPets
  ] = useState([]);

  const [
    searchTerm,
    setSearchTerm
  ] = useState("");

  const [
    selectedPetId,
    setSelectedPetId
  ] = useState("");

  const [
    dateFrom,
    setDateFrom
  ] = useState("");

  const [
    dateTo,
    setDateTo
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
    pet_id: "",
    visit_date: "",
    weight: "",
    diagnosis: "",
    treatment: "",
    notes: ""
  });

  const [
    editingMedicalRecordId,
    setEditingMedicalRecordId
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

  const canShowMedicalRecordForm =
    canCreateMedicalRecord() ||
    canEditMedicalRecord();

  const buildDateFromFilter =
    (value) => {

      if (!value) {

        return "";
      }

      return `${value} 00:00:00`;
    };

  const buildDateToFilter =
    (value) => {

      if (!value) {

        return "";
      }

      return `${value} 23:59:59`;
    };

  const fetchMedicalRecords =
    async (
      pageToLoad = page,
      filtersOverride = null
    ) => {

      try {

        setLoading(true);

        const filters =
          filtersOverride || {
            search: searchTerm.trim(),
            pet_id: selectedPetId,
            date_from: buildDateFromFilter(
              dateFrom
            ),
            date_to: buildDateToFilter(
              dateTo
            )
          };

        const data =
          await getPaginatedMedicalRecords({
            page: pageToLoad,
            page_size: pageSize,
            search: filters.search,
            pet_id: filters.pet_id,
            date_from: filters.date_from,
            date_to: filters.date_to
          });

        setMedicalRecords(
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
          "Error fetching medical records:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setLoading(false);
      }
    };

  const fetchPets =
    async () => {

      try {

        const data =
          await getPetsWithOwner();

        setPets(
          data
        );

      } catch (error) {

        console.error(
          "Error fetching pets:",
          error
        );

        setError(
          error.message
        );
      }
    };

  useEffect(() => {

    fetchPets();

  }, []);

  useEffect(() => {

    fetchMedicalRecords(
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
        pet_id: selectedPetId,
        date_from: buildDateFromFilter(
          dateFrom
        ),
        date_to: buildDateToFilter(
          dateTo
        )
      };

      await fetchMedicalRecords(
        1,
        filters
      );
    };

  const handleClearFilters =
    async () => {

      setError("");

      setSearchTerm("");
      setSelectedPetId("");
      setDateFrom("");
      setDateTo("");

      await fetchMedicalRecords(
        1,
        {
          search: "",
          pet_id: "",
          date_from: "",
          date_to: ""
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
        editingMedicalRecordId &&
        !canEditMedicalRecord()
      ) {

        setError(
          "You do not have permission to update medical records."
        );

        return;
      }

      if (
        !editingMedicalRecordId &&
        !canCreateMedicalRecord()
      ) {

        setError(
          "You do not have permission to create medical records."
        );

        return;
      }

      if (!formData.pet_id) {

        setError(
          "Please select a pet."
        );

        return;
      }

      if (!formData.visit_date) {

        setError(
          "Visit date is required."
        );

        return;
      }

      if (!formData.weight) {

        setError(
          "Weight is required."
        );

        return;
      }

      if (!formData.diagnosis.trim()) {

        setError(
          "Diagnosis is required."
        );

        return;
      }

      if (!formData.treatment.trim()) {

        setError(
          "Treatment is required."
        );

        return;
      }

      const payload = {
        pet_id: Number(
          formData.pet_id
        ),
        visit_date:
          formData.visit_date.replace(
            "T",
            " "
          ),
        weight: Number(
          formData.weight
        ),
        diagnosis:
          formData.diagnosis.trim(),
        treatment:
          formData.treatment.trim(),
        notes:
          formData.notes.trim()
      };

      try {

        setSaving(true);

        if (editingMedicalRecordId) {

          await updateMedicalRecord(
            editingMedicalRecordId,
            {
              visit_date:
                payload.visit_date,
              weight:
                payload.weight,
              diagnosis:
                payload.diagnosis,
              treatment:
                payload.treatment,
              notes:
                payload.notes
            }
          );

          toast.success(
            "Medical record updated successfully."
          );

        } else {

          await createMedicalRecord(
            payload
          );

          toast.success(
            "Medical record created successfully."
          );
        }

        setError("");

        resetForm();

        await fetchMedicalRecords(
          page
        );

      } catch (error) {

        console.error(
          "Error saving medical record:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setSaving(false);
      }
    };

  const handleEditMedicalRecord =
    (medicalRecord) => {

      if (!canEditMedicalRecord()) {

        setError(
          "You do not have permission to edit medical records."
        );

        return;
      }

      setEditingMedicalRecordId(
        medicalRecord.id
      );

      const formattedDate =
        medicalRecord.visit_date
          .replace(" ", "T")
          .slice(0, 16);

      setFormData({
        pet_id:
          medicalRecord.pet_id,
        visit_date:
          formattedDate,
        weight:
          medicalRecord.weight,
        diagnosis:
          medicalRecord.diagnosis,
        treatment:
          medicalRecord.treatment,
        notes:
          medicalRecord.notes || ""
      });

      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    };

  const handleDeleteMedicalRecord =
    async (medicalRecordId) => {

      if (!canDeleteMedicalRecord()) {

        setError(
          "You do not have permission to delete medical records."
        );

        return;
      }

      const confirmed =
        await openConfirmModal({
          title: "Delete medical record?",
          message: "This will permanently remove this clinical record from the pet history.",
          confirmText: "Delete Record",
          cancelText: "Keep Record",
          variant: "danger"
        });

      if (!confirmed) {

        return;
      }

      try {

        setDeletingId(
          medicalRecordId
        );

        await deleteMedicalRecord(
          medicalRecordId
        );

        toast.success(
          "Medical record deleted successfully."
        );

        setError("");

        await fetchMedicalRecords(
          page
        );

      } catch (error) {

        console.error(
          "Error deleting medical record:",
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

  const resetForm =
    () => {

      setEditingMedicalRecordId(
        null
      );

      setFormData({
        pet_id: "",
        visit_date: "",
        weight: "",
        diagnosis: "",
        treatment: "",
        notes: ""
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
            Medical Records
          </h1>

          <p className="page-subtitle">
            Track visit history, diagnoses, treatments, and clinical notes.
          </p>

        </div>

        <div className="page-summary-card">

          <span className="page-summary-number">
            {total}
          </span>

          <span className="page-summary-label">
            total records
          </span>

        </div>

      </div>

      {error && (

        <p className="error-message">
          {error}
        </p>

      )}

      {canShowMedicalRecordForm ? (

        <div className="card">

          <MedicalRecordForm
            formData={formData}
            handleChange={handleChange}
            handleSubmit={handleSubmit}
            editingMedicalRecordId={
              editingMedicalRecordId
            }
            resetForm={resetForm}
            pets={pets}
            saving={saving}
          />

        </div>

      ) : (

        <div className="card read-only-card">

          <h2>
            Read-only access
          </h2>

          <p>
            You can view medical records, but your role cannot create or update them.
          </p>

        </div>

      )}

      <div className="card">

        <div className="list-header">

          <div>

            <h2>
              Medical Record List
            </h2>

            <p>
              Search by diagnosis, treatment, notes, or pet, and filter by visit date.
            </p>

          </div>

        </div>

        <div className="advanced-filter-grid">

          <input
            type="text"
            placeholder="Search diagnosis, treatment, notes, or pet..."
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
            value={selectedPetId}
            onChange={(event) => {

              setError("");

              setSelectedPetId(
                event.target.value
              );

            }}
          >

            <option value="">
              All pets
            </option>

            {pets.map(
              (pet) => (

                <option
                  key={pet.id}
                  value={pet.id}
                >
                  {pet.name} ({pet.owner_name})
                </option>

              )
            )}

          </select>

          <input
            type="date"
            value={dateFrom}
            onChange={(event) => {

              setError("");

              setDateFrom(
                event.target.value
              );

            }}
          />

          <input
            type="date"
            value={dateTo}
            onChange={(event) => {

              setError("");

              setDateTo(
                event.target.value
              );

            }}
          />

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
            Loading medical records...
          </div>

        ) : (

          <>

            <MedicalRecordList
              medicalRecords={
                medicalRecords
              }
              pets={pets}
              editMedicalRecord={
                handleEditMedicalRecord
              }
              deleteMedicalRecord={
                handleDeleteMedicalRecord
              }
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

export default MedicalRecordsPage;