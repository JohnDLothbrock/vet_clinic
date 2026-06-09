import {
  useEffect,
  useState
} from "react";

import toast from "react-hot-toast";

import MedicalRecordForm from "../components/MedicalRecordForm";
import MedicalRecordList from "../components/MedicalRecordList";

import {
  getMedicalRecords,
  getMedicalRecordsByPet,
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
    selectedPetId,
    setSelectedPetId
  ] = useState("");

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

  const canShowMedicalRecordForm =
    canCreateMedicalRecord() ||
    canEditMedicalRecord();

  const fetchMedicalRecords =
    async () => {

      try {

        setLoading(true);

        const data =
          selectedPetId
            ? await getMedicalRecordsByPet(
              selectedPetId
            )
            : await getMedicalRecords();

        setMedicalRecords(
          data
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

    fetchMedicalRecords();

  }, [
    selectedPetId
  ]);

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

        await fetchMedicalRecords();

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
        window.confirm(
          "Are you sure you want to delete this medical record?"
        );

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

        await fetchMedicalRecords();

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

      <h1 className="title">
        Medical Records
      </h1>

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

        <div className="card">

          <p>
            You have read-only access to medical records.
          </p>

        </div>

      )}

      <div className="card">

        <h2>
          Medical Record List
        </h2>

        <div className="filter-row">

          <select
            value={selectedPetId}
            onChange={(event) => {
              setSelectedPetId(
                event.target.value
              );
            }}
          >

            <option value="">
              All Pets
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

          <button
            type="button"
            onClick={() => {
              setSelectedPetId("");
            }}
          >
            Clear Filter
          </button>

        </div>

        {loading ? (

          <p>
            Loading medical records...
          </p>

        ) : (

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

        )}

      </div>

    </div>
  );
}

export default MedicalRecordsPage;