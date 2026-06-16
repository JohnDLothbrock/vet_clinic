import {
  useEffect,
  useState
} from "react";

import toast from "react-hot-toast";

import AppointmentForm from "../components/AppointmentForm";
import AppointmentList from "../components/AppointmentList";
import ConfirmModal from "../components/ConfirmModal";

import useConfirmModal from "../hooks/useConfirmModal";

import {
  getAppointments,
  createAppointment,
  updateAppointment,
  deleteAppointment
} from "../services/appointmentService";

import {
  getPetsWithOwner
} from "../services/petService";

import {
  canCreateAppointment,
  canEditAppointment,
  canDeleteAppointment
} from "../services/permissionService";

import "../styles/app.css";

function AppointmentsPage() {

  const [
    appointments,
    setAppointments
  ] = useState([]);

  const [
    pets,
    setPets
  ] = useState([]);

  const [
    formData,
    setFormData
  ] = useState({
    pet_id: "",
    appointment_date: "",
    reason: ""
  });

  const [
    editingAppointmentId,
    setEditingAppointmentId
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

  const canShowAppointmentForm =
    canCreateAppointment() ||
    canEditAppointment();

  const fetchAppointments =
    async () => {

      try {

        setLoading(true);

        const data =
          await getAppointments();

        setAppointments(
          data
        );

        setError("");

      } catch (error) {

        console.error(
          "Error fetching appointments:",
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
      }
    };

  useEffect(() => {

    fetchAppointments();
    fetchPets();

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

  const handleSubmit =
    async (event) => {

      event.preventDefault();

      if (saving) {

        return;
      }

      if (
        editingAppointmentId &&
        !canEditAppointment()
      ) {

        setError(
          "You do not have permission to update appointments."
        );

        return;
      }

      if (
        !editingAppointmentId &&
        !canCreateAppointment()
      ) {

        setError(
          "You do not have permission to create appointments."
        );

        return;
      }

      if (!formData.pet_id) {

        setError(
          "Please select a pet."
        );

        return;
      }

      if (!formData.appointment_date) {

        setError(
          "Appointment date is required."
        );

        return;
      }

      if (!formData.reason.trim()) {

        setError(
          "Reason is required."
        );

        return;
      }

      const payload = {
        pet_id:
          Number(formData.pet_id),

        appointment_date:
          formData.appointment_date.replace(
            "T",
            " "
          ),

        reason:
          formData.reason.trim()
      };

      try {

        setSaving(true);

        if (
          editingAppointmentId
        ) {

          await updateAppointment(
            editingAppointmentId,
            {
              appointment_date:
                payload.appointment_date,

              reason:
                payload.reason
            }
          );

          toast.success(
            "Appointment updated successfully."
          );

        } else {

          await createAppointment(
            payload
          );

          toast.success(
            "Appointment created successfully."
          );
        }

        setError("");

        resetForm();

        await fetchAppointments();

      } catch (error) {

        console.error(
          "Error saving appointment:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setSaving(false);
      }
    };

  const handleDeleteAppointment =
    async (appointmentId) => {

      if (!canDeleteAppointment()) {

        setError(
          "You do not have permission to delete appointments."
        );

        return;
      }

      const confirmed =
        await openConfirmModal({
          title: "Delete appointment?",
          message: "This will permanently remove this appointment from the schedule.",
          confirmText: "Delete Appointment",
          cancelText: "Keep Appointment",
          variant: "danger"
        });

      if (!confirmed) {

        return;
      }

      try {

        setDeletingId(
          appointmentId
        );

        await deleteAppointment(
          appointmentId
        );

        toast.success(
          "Appointment deleted successfully."
        );

        setError("");

        await fetchAppointments();

      } catch (error) {

        console.error(
          "Error deleting appointment:",
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

  const handleEditAppointment =
    (appointment) => {

      if (!canEditAppointment()) {

        setError(
          "You do not have permission to edit appointments."
        );

        return;
      }

      setEditingAppointmentId(
        appointment.id
      );

      const formattedDate =
        appointment.appointment_date
          .replace(" ", "T")
          .slice(0, 16);

      setFormData({
        pet_id:
          appointment.pet_id,

        appointment_date:
          formattedDate,

        reason:
          appointment.reason
      });

      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    };

  const resetForm =
    () => {

      setEditingAppointmentId(
        null
      );

      setFormData({
        pet_id: "",
        appointment_date: "",
        reason: ""
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
            Appointments
          </h1>

          <p className="page-subtitle">
            Schedule, update, and review upcoming clinic visits.
          </p>

        </div>

        <div className="page-summary-card">

          <span className="page-summary-number">
            {appointments.length}
          </span>

          <span className="page-summary-label">
            appointments shown
          </span>

        </div>

      </div>

      {error && (

        <p className="error-message">
          {error}
        </p>

      )}

      {canShowAppointmentForm ? (

        <AppointmentForm
          formData={formData}
          handleChange={handleChange}
          handleSubmit={handleSubmit}
          editingAppointmentId={
            editingAppointmentId
          }
          resetForm={resetForm}
          pets={pets}
          saving={saving}
        />

      ) : (

        <div className="card read-only-card">

          <h2>
            Read-only access
          </h2>

          <p>
            You can view appointments, but your role cannot create or update them.
          </p>

        </div>

      )}

      <div className="card">

        <div className="list-header">

          <div>

            <h2>
              Appointment List
            </h2>

            <p>
              Review scheduled appointments and visit reasons.
            </p>

          </div>

        </div>

        {loading ? (

          <div className="loading-card">
            Loading appointments...
          </div>

        ) : (

          <AppointmentList
            appointments={appointments}
            editAppointment={
              handleEditAppointment
            }
            deleteAppointment={
              handleDeleteAppointment
            }
            deletingId={deletingId}
          />

        )}

      </div>

    </div>
  );
}

export default AppointmentsPage;