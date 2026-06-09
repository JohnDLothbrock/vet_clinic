import {
  useEffect,
  useState
} from "react";

import toast from "react-hot-toast";

import AppointmentForm from "../components/AppointmentForm";
import AppointmentList from "../components/AppointmentList";

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

  const canShowAppointmentForm =
    canCreateAppointment() ||
    canEditAppointment();

  const fetchAppointments =
    async () => {

      try {

        setLoading(true);

        const data =
          await getAppointments();

        setAppointments(data);

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

        setPets(data);

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
        window.confirm(
          "Are you sure you want to delete this appointment?"
        );

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

  const resetForm = () => {

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

      <h1>
        Appointments
      </h1>

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

        <div className="card">

          <p>
            You have read-only access to appointments.
          </p>

        </div>

      )}

      {loading ? (

        <p>
          Loading appointments...
        </p>

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
  );
}

export default AppointmentsPage;