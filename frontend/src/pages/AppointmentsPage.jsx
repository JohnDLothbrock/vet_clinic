import {
  useEffect,
  useState
} from "react";

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

  // LOAD APPOINTMENTS
  const fetchAppointments =
    async () => {

      try {

        const data =
          await getAppointments();

        setAppointments(data);

      } catch (error) {

        console.error(
          "Error fetching appointments:",
          error
        );
      }
    };

  // LOAD PETS
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

  // INPUTS
  const handleChange = (
    event
  ) => {

    setFormData({
      ...formData,
      [event.target.name]:
        event.target.value
    });
  };

  // CREATE / UPDATE
  const handleSubmit =
    async (event) => {

      event.preventDefault();

      const payload = {

        pet_id:
          Number(formData.pet_id),

        appointment_date:
          formData.appointment_date,

        reason:
          formData.reason
      };

      try {

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

        } else {

          await createAppointment(
            payload
          );
        }

        resetForm();

        fetchAppointments();

      } catch (error) {

        console.error(
          "Error saving appointment:",
          error
        );
      }
    };

  // DELETE
  const handleDeleteAppointment =
    async (appointmentId) => {

      try {

        await deleteAppointment(
          appointmentId
        );

        fetchAppointments();

      } catch (error) {

        console.error(
          "Error deleting appointment:",
          error
        );
      }
    };

  // EDIT
  const handleEditAppointment =
    (appointment) => {

      setEditingAppointmentId(
        appointment.id
      );

      setFormData({
        pet_id:
          appointment.pet_id,

        appointment_date:
          appointment.appointment_date,

        reason:
          appointment.reason
      });

      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    };

  // RESET
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

      <AppointmentForm
        formData={formData}
        handleChange={handleChange}
        handleSubmit={handleSubmit}
        editingAppointmentId={
          editingAppointmentId
        }
        resetForm={resetForm}
        pets={pets}
      />

      <AppointmentList
        appointments={appointments}
        editAppointment={
          handleEditAppointment
        }
        deleteAppointment={
          handleDeleteAppointment
        }
      />

    </div>
  );
}

export default AppointmentsPage;